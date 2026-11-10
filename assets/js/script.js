/**
 * ==============================================================================
 * CampusConnect AI - Client JavaScript Engine
 * Technology: Vanilla JavaScript (ES6+)
 * Objective: UI Interactions, Category Filtering & Botpress Integration Hooks
 * ==============================================================================
 */

document.addEventListener('DOMContentLoaded', () => {
  'use strict';

  console.log('[CampusConnect AI] Frontend portal initialized.');
  console.log('[CampusConnect AI] Architecture prepared for Botpress Cloud Webchat integration.');

  // --- 1. Mobile Navigation Toggle ---
  const mobileToggle = document.getElementById('mobileToggle');
  const navMenu = document.getElementById('navMenu');

  if (mobileToggle && navMenu) {
    mobileToggle.addEventListener('click', () => {
      const isOpen = navMenu.classList.toggle('open');
      mobileToggle.setAttribute('aria-expanded', String(isOpen));
    });

    // Close menu when clicking outside or on a link
    document.addEventListener('click', (event) => {
      if (!mobileToggle.contains(event.target) && !navMenu.contains(event.target)) {
        navMenu.classList.remove('open');
        mobileToggle.setAttribute('aria-expanded', 'false');
      }
    });

    navMenu.querySelectorAll('.nav-link').forEach((link) => {
      link.addEventListener('click', () => {
        navMenu.classList.remove('open');
        mobileToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // --- 2. Interactive Guidance Category Filter ---
  const filterButtons = document.querySelectorAll('.filter-btn');
  const guidanceCards = document.querySelectorAll('.guidance-card');

  if (filterButtons.length && guidanceCards.length) {
    filterButtons.forEach((btn) => {
      btn.addEventListener('click', () => {
        // Toggle active button
        filterButtons.forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');

        const category = btn.getAttribute('data-category');

        guidanceCards.forEach((card) => {
          const cardCategory = card.getAttribute('data-category');
          if (category === 'all' || cardCategory === category) {
            card.style.display = 'flex';
            card.style.animation = 'fadeIn 0.25s ease';
          } else {
            card.style.display = 'none';
          }
        });
      });
    });
  }

  // --- 3. Stage 1 Botpress Integration Status Modal ---
  const modalOverlay = document.getElementById('noticeModalOverlay');
  const modalCloseBtn = document.getElementById('modalCloseBtn');
  const modalAcknowledgeBtn = document.getElementById('modalAcknowledgeBtn');
  const triggerButtons = document.querySelectorAll('[data-trigger="assistant-status"]');

  function openNoticeModal() {
    if (modalOverlay) {
      modalOverlay.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeNoticeModal() {
    if (modalOverlay) {
      modalOverlay.classList.remove('active');
      document.body.style.overflow = '';
    }
  }

  triggerButtons.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      openNoticeModal();
    });
  });

  if (modalCloseBtn) {
    modalCloseBtn.addEventListener('click', closeNoticeModal);
  }

  if (modalAcknowledgeBtn) {
    modalAcknowledgeBtn.addEventListener('click', closeNoticeModal);
  }

  if (modalOverlay) {
    modalOverlay.addEventListener('click', (e) => {
      if (e.target === modalOverlay) {
        closeNoticeModal();
      }
    });
  }

  // --- 4. Botpress Cloud Webchat Integration Stub ---
  /**
   * Initializes the official Botpress Cloud Webchat embed.
   * This function will be invoked when Botpress credentials are wired in Stage 2/4.
   * 
   * @param {Object} config - Configuration object containing botId and clientId
   */
  window.initBotpressWebchat = function (config) {
    if (!config || !config.botId) {
      console.warn('[CampusConnect AI] Botpress Webchat config missing botId. Integration pending.');
      return;
    }

    console.log('[CampusConnect AI] Initializing Botpress Webchat with Bot ID:', config.botId);

    // Dynamic injection of official Botpress Webchat script bundle
    const injectScript = document.createElement('script');
    injectScript.src = 'https://cdn.botpress.cloud/webchat/v2/inject.js';
    injectScript.async = true;
    injectScript.onload = () => {
      console.log('[CampusConnect AI] Botpress inject.js loaded successfully.');
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
