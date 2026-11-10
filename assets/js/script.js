/**
 * ==============================================================================
 * CampusConnect AI - Master Client JavaScript Engine
 * Technologies: Pure Vanilla JavaScript (ES6+)
 * Objective: Navigation, Accessibility, Interactive Inquiries & Botpress Hooks
 * ==============================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  'use strict';

  console.log('[CampusConnect AI] Client portal engine initialized.');
  console.log('[CampusConnect AI] Botpress Webchat integration hook: window.initBotpressWebchat(config).');

  // --- 1. Mobile Navigation Drawer & Hamburger ---
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

  // --- 2. Active Navigation Spy (Scroll Observer) ---
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

  // --- 3. Assistant Modal Management ---
  const assistantModal = document.getElementById('assistantModal');
  const modalCloseBtn = document.getElementById('modalCloseBtn');
  const modalCloseActionBtn = document.getElementById('modalCloseActionBtn');
  const selectedQueryBox = document.getElementById('selectedQueryBox');
  const selectedQueryText = document.getElementById('selectedQueryText');
  const openModalTriggers = document.querySelectorAll('[data-trigger="chatbot-modal"]');

  /**
   * Opens the assistant status modal.
   * Optionally populates a selected user question.
   * 
   * @param {string} [question] - Optional question string selected by the user
   */
  function openAssistantModal(question = '') {
    if (!assistantModal) return;

    if (question && selectedQueryBox && selectedQueryText) {
      selectedQueryText.textContent = `"${question}"`;
      selectedQueryBox.style.display = 'block';
      console.log(`[CampusConnect AI] Question primed for Botpress: "${question}"`);
    } else if (selectedQueryBox) {
      selectedQueryBox.style.display = 'none';
    }

    assistantModal.classList.add('active');
    assistantModal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';

    // Focus close button for accessibility
    if (modalCloseBtn) {
      modalCloseBtn.focus();
    }
  }

  /**
   * Closes the assistant status modal.
   */
  function closeAssistantModal() {
    if (!assistantModal) return;

    assistantModal.classList.remove('active');
    assistantModal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  // Bind trigger buttons (Hero, Nav, Floating button, Showcase button)
  openModalTriggers.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openAssistantModal();
    });
  });

  // Bind modal close buttons
  if (modalCloseBtn) modalCloseBtn.addEventListener('click', closeAssistantModal);
  if (modalCloseActionBtn) modalCloseActionBtn.addEventListener('click', closeAssistantModal);

  // Close on backdrop click
  if (assistantModal) {
    assistantModal.addEventListener('click', (e) => {
      if (e.target === assistantModal) {
        closeAssistantModal();
      }
    });
  }

  // Close on Escape key press
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && assistantModal && assistantModal.classList.contains('active')) {
      closeAssistantModal();
    }
  });

  // --- 4. Interactive Suggested Question Cards ---
  const questionCards = document.querySelectorAll('.question-card');
  const categoryQuestionButtons = document.querySelectorAll('[data-question]');

  /**
   * Dispatches inquiry to Botpress or opens status modal if Botpress is pending.
   * 
   * @param {string} question - Question query string
   */
  function handleQuestionInquiry(question) {
    if (!question) return;

    // Check if Botpress Webchat is actively connected
    if (window.botpress && typeof window.botpress.sendEvent === 'function') {
      console.log('[CampusConnect AI] Dispatching message to connected Botpress instance:', question);
      window.botpress.sendEvent({
        type: 'message',
        text: question
      });
      if (typeof window.botpress.open === 'function') {
        window.botpress.open();
      }
      return;
    }

    // Botpress is in Standby mode -> Show modal with question displayed
    openAssistantModal(question);
  }

  questionCards.forEach((card) => {
    card.addEventListener('click', () => {
      const question = card.getAttribute('data-question') || card.querySelector('.question-text')?.textContent.replace(/[""]/g, '');
      handleQuestionInquiry(question);
    });

    // Make question cards keyboard accessible
    card.setAttribute('tabindex', '0');
    card.setAttribute('role', 'button');
    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        const question = card.getAttribute('data-question') || card.querySelector('.question-text')?.textContent.replace(/[""]/g, '');
        handleQuestionInquiry(question);
      }
    });
  });

  categoryQuestionButtons.forEach((btn) => {
    btn.addEventListener('click', () => {
      const question = btn.getAttribute('data-question');
      handleQuestionInquiry(question);
    });
  });

  // --- 5. Clean Integration Hook for Botpress Cloud Webchat ---
  /**
   * Initializes the official Botpress Cloud Webchat v2 embed.
   * Call this function when actual botId and clientId are supplied.
   * 
   * @param {Object} config - Configuration object containing botId, clientId, etc.
   */
  window.initBotpressWebchat = function (config) {
    if (!config || !config.botId) {
      console.warn('[CampusConnect AI] Botpress Webchat configuration missing botId. Bot remains in Standby mode.');
      return;
    }

    console.log('[CampusConnect AI] Connecting live Botpress Cloud Webchat:', config.botId);

    // Update connection indicator in UI
    const connectionIndicator = document.getElementById('botpressConnectionIndicator');
    const pulseDot = document.querySelector('.pulse-dot');
    if (connectionIndicator) {
      connectionIndicator.textContent = 'Botpress Cloud: Connected (Live Assistant)';
    }
    if (pulseDot) {
      pulseDot.classList.remove('standby');
      pulseDot.classList.add('ready');
    }

    // Inject official Botpress Webchat script bundle
    const injectScript = document.createElement('script');
    injectScript.src = 'https://cdn.botpress.cloud/webchat/v2/inject.js';
    injectScript.async = true;
    injectScript.onload = () => {
      console.log('[CampusConnect AI] Botpress Webchat bundle loaded.');
      if (window.botpress) {
        window.botpress.init({
          botId: config.botId,
          clientId: config.clientId || config.botId,
          hostUrl: config.hostUrl || 'https://cdn.botpress.cloud/webchat/v2',
          messagingUrl: config.messagingUrl || 'https://messaging.botpress.cloud',
          botName: config.botName || 'CampusConnect AI',
          botDescription: 'Generative AI Student Assistance Chatbot'
        });
      }
    };
    document.body.appendChild(injectScript);
  };
});
