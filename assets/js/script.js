/**
 * ==============================================================================
 * CampusConnect AI - Master Client JavaScript Engine
 * Technologies: Pure Vanilla JavaScript (ES6+)
 * Objective: Navigation, Accessibility, Interactive Inquiries & Official Botpress Webchat
 * ==============================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  'use strict';

  console.log('[CampusConnect AI] Client portal engine initialized.');

  // --- 1. Botpress Webchat Integration State & Event Binding ---
  let isWebchatReady = false;
  let pendingQuestion = null;

  /**
   * Called when Botpress Webchat fires the 'webchat:ready' event.
   */
  function handleBotpressReady() {
    if (isWebchatReady) return;
    isWebchatReady = true;
    console.log('[CampusConnect AI] Official Botpress Webchat is connected and ready.');

    // Update announcement bar indicator
    const connectionIndicator = document.getElementById('botpressConnectionIndicator');
    if (connectionIndicator) {
      connectionIndicator.textContent = 'Botpress Cloud: Connected (Live Assistant)';
    }

    // Update pulse dots to ready (green)
    const pulseDots = document.querySelectorAll('.pulse-dot');
    pulseDots.forEach((dot) => {
      dot.classList.remove('standby');
      dot.classList.add('ready');
    });

    // Update chatbot section status pill
    const statusPill = document.getElementById('chatbotStatusPill');
    if (statusPill) {
      statusPill.classList.remove('standby');
      statusPill.classList.add('ready');
      statusPill.innerHTML = '<span class="status-indicator-dot ready"></span><span><strong>Status:</strong> Botpress Webchat Connected & Live</span>';
    }

    // Hide custom floating button to prevent duplicate chatbot widgets
    const floatingBtn = document.getElementById('floatingAssistantTrigger');
    if (floatingBtn) {
      floatingBtn.style.display = 'none';
    }

    // If user clicked a suggested question while loading, dispatch it now
    if (pendingQuestion) {
      const queuedQuestion = pendingQuestion;
      pendingQuestion = null;
      console.log(`[CampusConnect AI] Dispatching queued question to Webchat: "${queuedQuestion}"`);
      dispatchMessageToBotpress(queuedQuestion);
    }
  }

  /**
   * Dispatches a message to Botpress Webchat using official methods.
   * Ensures the Webchat is opened first, then delivers the message.
   * 
   * @param {string} message - Message text to send
   */
  function dispatchMessageToBotpress(message) {
    if (!message) return;

    if (window.botpress && typeof window.botpress.open === 'function') {
      try {
        // Open the Webchat window
        window.botpress.open();

        // If Webchat is fully ready, send the message using official sendMessage
        if (isWebchatReady && typeof window.botpress.sendMessage === 'function') {
          console.log(`[CampusConnect AI] Calling window.botpress.sendMessage("${message}")`);
          window.botpress.sendMessage(message);
        } else {
          // If open but not yet fully ready, queue for the readiness event
          pendingQuestion = message;
        }
      } catch (err) {
        console.error('[CampusConnect AI] Error interacting with Botpress Webchat:', err);
        openFallbackModal(message);
      }
    } else {
      console.warn('[CampusConnect AI] Botpress Webchat not available. Opening fallback dialog.');
      openFallbackModal(message);
    }
  }

  /**
   * Opens the Botpress Webchat interface.
   */
  function openBotpressChat() {
    if (window.botpress && typeof window.botpress.open === 'function') {
      try {
        console.log('[CampusConnect AI] Calling window.botpress.open()');
        window.botpress.open();
      } catch (err) {
        console.error('[CampusConnect AI] Error calling window.botpress.open():', err);
        openFallbackModal();
      }
    } else {
      console.warn('[CampusConnect AI] Botpress Webchat not initialized yet.');
      openFallbackModal();
    }
  }

  /**
   * Initializes listeners on window.botpress once available.
   */
  function initBotpressListeners() {
    if (window.botpress && typeof window.botpress.on === 'function') {
      try {
        window.botpress.on('webchat:ready', () => {
          handleBotpressReady();
        });

        window.botpress.on('webchat:opened', () => {
          console.log('[CampusConnect AI] Botpress Webchat opened by user.');
        });

        window.botpress.on('webchat:closed', () => {
          console.log('[CampusConnect AI] Botpress Webchat closed by user.');
        });

        // If already loaded before listener attachment
        if (window.botpress.isLoaded) {
          handleBotpressReady();
        }
      } catch (e) {
        console.warn('[CampusConnect AI] Could not attach Botpress event listener:', e);
      }
    } else {
      // Poll every 100ms up to 10 seconds for delayed script loading
      let attempts = 0;
      const pollInterval = setInterval(() => {
        attempts++;
        if (window.botpress && typeof window.botpress.on === 'function') {
          clearInterval(pollInterval);
          try {
            window.botpress.on('webchat:ready', () => {
              handleBotpressReady();
            });
            if (window.botpress.isLoaded) {
              handleBotpressReady();
            }
          } catch (e) {
            console.warn('[CampusConnect AI] Botpress listener error during polling:', e);
          }
        } else if (attempts >= 100) { // 10 seconds
          clearInterval(pollInterval);
          console.warn('[CampusConnect AI] Botpress Webchat script load timeout or network offline.');
        }
      }, 100);
    }
  }

  // Start listener setup
  initBotpressListeners();

  // --- 2. Mobile Navigation Drawer & Hamburger ---
  const mobileToggle = document.getElementById('mobileToggle');
  const navMenu = document.getElementById('navMenu');
  const navLinks = document.querySelectorAll('.nav-link');

  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', () => {
      const isExpanded = navMenu.classList.toggle('open');
      mobileToggle.classList.toggle('active', isExpanded);
      mobileToggle.setAttribute('aria-expanded', String(isExpanded));
    });

    // Close mobile menu on outside click
    document.addEventListener('click', (event) => {
      if (!mobileToggle.contains(event.target) && !navMenu.contains(event.target)) {
        navMenu.classList.remove('open');
        mobileToggle.classList.remove('active');
        mobileToggle.setAttribute('aria-expanded', 'false');
      }
    });

    // Close mobile menu when clicking any nav link
    navLinks.forEach((link) => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('open');
        mobileToggle.classList.remove('active');
        mobileToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // --- 3. Active Navigation Spy (Scroll Observer) ---
  const sections = document.querySelectorAll('main > section[id]');

  if ('IntersectionObserver' in window && sections.length > 0) {
    const observerOptions = {
      root: null,
      rootMargin: '-20% 0px -70% 0px',
      threshold: 0
    };

    const sectionObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const currentId = entry.target.getAttribute('id');
          navLinks.forEach((link) => {
            const href = link.getAttribute('href');
            if (href === `#${currentId}`) {
              link.classList.add('active');
            } else {
              link.classList.remove('active');
            }
          });
        }
      });
    }, observerOptions);

    sections.forEach((section) => sectionObserver.observe(section));
  }

  // --- 4. Fallback Modal Dialog Management ---
  const assistantModal = document.getElementById('assistantModal');
  const modalCloseBtn = document.getElementById('modalCloseBtn');
  const modalCloseActionBtn = document.getElementById('modalCloseActionBtn');
  const selectedQueryBox = document.getElementById('selectedQueryBox');
  const selectedQueryText = document.getElementById('selectedQueryText');

  /**
   * Opens the fallback dialog if Botpress Webchat is unavailable.
   * 
   * @param {string} [question] - Optional question string selected by the user
   */
  function openFallbackModal(question = '') {
    if (!assistantModal) return;

    if (question && selectedQueryBox && selectedQueryText) {
      selectedQueryText.textContent = `"${question}"`;
      selectedQueryBox.style.display = 'block';
    } else if (selectedQueryBox) {
      selectedQueryBox.style.display = 'none';
    }

    assistantModal.classList.add('active');
    assistantModal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';

    if (modalCloseBtn) {
      modalCloseBtn.focus();
    }
  }

  /**
   * Closes the fallback dialog.
   */
  function closeFallbackModal() {
    if (!assistantModal) return;

    assistantModal.classList.remove('active');
    assistantModal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  if (modalCloseBtn) modalCloseBtn.addEventListener('click', closeFallbackModal);
  if (modalCloseActionBtn) modalCloseActionBtn.addEventListener('click', closeFallbackModal);

  if (assistantModal) {
    assistantModal.addEventListener('click', (e) => {
      if (e.target === assistantModal) {
        closeFallbackModal();
      }
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && assistantModal && assistantModal.classList.contains('active')) {
      closeFallbackModal();
    }
  });

  // --- 5. Connecting CTA Buttons to Official Botpress Webchat ---
  // Elements: "Ask AI" in nav, "Ask CampusConnect" in hero, "Open AI Chatbot" in section 4, preview CTA
  const askButtons = document.querySelectorAll('#navAskAiBtn, #heroAskBtn, #mainOpenChatbotBtn, .preview-cta-btn, #floatingAssistantTrigger');

  askButtons.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      // If Webchat is ready or available, open it directly using official method
      if (window.botpress && typeof window.botpress.open === 'function') {
        openBotpressChat();
      } else {
        // Fallback if script is blocked or still loading
        openFallbackModal();
      }
    });
  });

  // --- 6. Connecting Suggested Question Cards to Official Botpress Webchat ---
  const questionCards = document.querySelectorAll('.question-card');
  const categoryQuestionButtons = document.querySelectorAll('[data-question]');

  function handleQuestionClick(question) {
    if (!question) return;

    console.log(`[CampusConnect AI] User selected suggested question: "${question}"`);

    if (window.botpress && typeof window.botpress.open === 'function') {
      dispatchMessageToBotpress(question);
    } else {
      openFallbackModal(question);
    }
  }

  questionCards.forEach((card) => {
    card.addEventListener('click', () => {
      const question = card.getAttribute('data-question') || card.querySelector('.question-text')?.textContent.replace(/[""]/g, '');
      handleQuestionClick(question);
    });

    // Keyboard accessibility
    card.setAttribute('tabindex', '0');
    card.setAttribute('role', 'button');
    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        const question = card.getAttribute('data-question') || card.querySelector('.question-text')?.textContent.replace(/[""]/g, '');
        handleQuestionClick(question);
      }
    });
  });

  categoryQuestionButtons.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const question = btn.getAttribute('data-question');
      handleQuestionClick(question);
    });
  });

  // --- 7. Backward Compatibility / Global Helper Hook ---
  window.initBotpressWebchat = function (config) {
    console.log('[CampusConnect AI] initBotpressWebchat hook called. Webchat bundle is embedded in index.html.');
    if (window.botpress && typeof window.botpress.open === 'function') {
      window.botpress.open();
    }
  };
});
