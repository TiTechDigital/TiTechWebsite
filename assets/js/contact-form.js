/* Contact form with Resend API integration
   Handles form submission via serverless function instead of mailto */
(() => {
  'use strict';

  // Select all contact forms (homepage and dedicated contact pages)
  const forms = document.querySelectorAll('.contact__form, form[data-mailto-form]');

  forms.forEach(form => {
    const statusElement = form.querySelector('.contact__status, .form__status');
    const submitButton = form.querySelector('button[type="submit"]');
    const language = document.documentElement.lang === 'en' ? 'en' : 'it';

    // Messages
    const messages = {
      it: {
        sending: 'Invio in corso...',
        success: 'Richiesta ricevuta.',
        error: 'Scrivi a info@titechdigital.it per inviare la richiesta.',
        incomplete: 'Inserisci il nome, un indirizzo email valido e una descrizione del progetto.',
        invalidEmail: 'Inserisci un indirizzo email valido.'
      },
      en: {
        sending: 'Sending...',
        success: 'Enquiry received.',
        error: 'Email info@titechdigital.it to send your enquiry.',
        incomplete: 'Please fill in your name, email and message: those are the three fields we need in order to reply.',
        invalidEmail: 'Please enter a valid email address.'
      }
    };

    const msg = messages[language];

    // Update status message
    const updateStatus = (message, state = '') => {
      if (!statusElement) return;
      statusElement.textContent = message;
      statusElement.dataset.state = state;
      
      // Also update aria-live for accessibility
      if (state === 'error') {
        statusElement.setAttribute('role', 'alert');
      } else {
        statusElement.setAttribute('role', 'status');
      }
    };

    // Validate email
    const isValidEmail = (email) => {
      const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return regex.test(email);
    };

    // Handle form submission
    form.addEventListener('submit', async (event) => {
      event.preventDefault();

      // Get form data
      const formData = new FormData(form);
      const name = formData.get('name')?.trim() || '';
      const email = formData.get('email')?.trim() || '';
      const message = formData.get('message')?.trim() || '';
      const phone = formData.get('phone')?.trim() || '';
      const company = formData.get('company')?.trim() || '';
      const service = formData.get('topic') || formData.get('service') || '';

      // Validate required fields
      if (!name || !email || !message) {
        updateStatus(msg.incomplete, 'error');
        return;
      }

      // Validate email format
      if (!isValidEmail(email)) {
        updateStatus(msg.invalidEmail, 'error');
        return;
      }

      // Disable submit button and show sending state
      if (submitButton) {
        submitButton.disabled = true;
        submitButton.setAttribute('aria-busy', 'true');
      }
      updateStatus(msg.sending, 'sending');

      // Collect attribution data if available
      const attr = window.titechAttribution || {};
      const attribution = {
        source: attr.source,
        medium: attr.medium,
        campaign: attr.campaign,
        landing: attr.landing,
        referrer: attr.referrer
      };

      // Prepare payload
      const payload = {
        name,
        email,
        message,
        phone,
        company,
        service,
        language,
        attribution
      };

      try {
        // Send to API
        const response = await fetch('/api/send-email', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (response.ok) {
          // Success
          updateStatus(msg.success, 'ok');
          
          // Reset form after successful submission
          form.reset();

          // Track conversion for any active A/B test
          if (window.titechExperimentConvert) {
            Object.keys((window.titechExperiments || {}).assignments || {}).forEach(name => {
              window.titechExperimentConvert(name);
            });
          }

          // Dispatch custom event for analytics
          document.dispatchEvent(new CustomEvent('titech:contact-submit', { 
            detail: { 
              form: form.classList.contains('contact__form') ? 'contact_homepage' : 'contact_page',
              method: 'api'
            } 
          }));

        } else {
          // Server returned an error
          updateStatus(data.error || msg.error, 'error');
        }

      } catch (error) {
        // Network or other error
        console.error('Form submission error:', error);
        updateStatus(msg.error, 'error');

      } finally {
        // Re-enable submit button
        if (submitButton) {
          submitButton.disabled = false;
          submitButton.removeAttribute('aria-busy');
        }
      }
    });
  });
})();
