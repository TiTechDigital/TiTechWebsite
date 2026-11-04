/* Code protection - Makes it harder to inspect and copy code
   Note: This is NOT foolproof security. Determined users can still access the code.
   This only deters casual copying. 
   Enhanced with multiple detection methods and automatic redirect. */

(function() {
  'use strict';

  let devtoolsOpen = false;
  let warningShown = false;
  const threshold = 160;

  // Function to blur page and show warning
  const blockAccess = () => {
    if (warningShown) return;
    warningShown = true;
    
    // Blur the page content
    document.documentElement.style.filter = 'blur(10px)';
    document.body.style.userSelect = 'none';
    document.body.style.pointerEvents = 'none';
    
    // Show warning overlay
    const overlay = document.createElement('div');
    overlay.id = 'devtools-warning';
    overlay.style.cssText = `
      position: fixed;
      inset: 0;
      z-index: 2147483647;
      background: rgba(16, 25, 35, 0.98);
      color: #f7f8f6;
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: system-ui, sans-serif;
      text-align: center;
      padding: 20px;
    `;
    overlay.innerHTML = `
      <div style="max-width: 400px;">
        <h2 style="font-size: 24px; margin: 0 0 16px 0;">⚠️ Accesso non autorizzato</h2>
        <p style="font-size: 16px; line-height: 1.5; margin: 0 0 20px 0;">
          Gli strumenti di sviluppo sono disabilitati per proteggere il codice proprietario.
        </p>
        <p style="font-size: 14px; opacity: 0.7; margin: 0;">
          Developer tools are disabled to protect proprietary code.
        </p>
      </div>
    `;
    document.body.appendChild(overlay);
    
    // Redirect after 1.5 seconds
    setTimeout(() => {
      window.location.href = '/';
    }, 1500);
  };

  // Disable right-click context menu - multiple layers
  document.addEventListener('contextmenu', function(e) {
    e.preventDefault();
    e.stopPropagation();
    return false;
  }, true);
  
  // Also block on window
  window.addEventListener('contextmenu', function(e) {
    e.preventDefault();
    return false;
  });
  
  // Block on specific elements
  document.addEventListener('DOMContentLoaded', function() {
    document.body.addEventListener('contextmenu', function(e) {
      e.preventDefault();
      return false;
    });
  });

  // Disable common developer shortcuts
  document.addEventListener('keydown', function(e) {
    // F12 key
    if (e.keyCode === 123) {
      e.preventDefault();
      return false;
    }
    
    // Ctrl+Shift+I (DevTools)
    if (e.ctrlKey && e.shiftKey && e.keyCode === 73) {
      e.preventDefault();
      return false;
    }
    
    // Ctrl+Shift+J (Console)
    if (e.ctrlKey && e.shiftKey && e.keyCode === 74) {
      e.preventDefault();
      return false;
    }
    
    // Ctrl+Shift+C (Inspect Element)
    if (e.ctrlKey && e.shiftKey && e.keyCode === 67) {
      e.preventDefault();
      return false;
    }
    
    // Ctrl+U (View Source)
    if (e.ctrlKey && e.keyCode === 85) {
      e.preventDefault();
      return false;
    }
    
    // Ctrl+S (Save Page)
    if (e.ctrlKey && e.keyCode === 83) {
      e.preventDefault();
      return false;
    }
  }, false);

  // Detect if DevTools is open via window size changes
  const checkDevTools = () => {
    const widthThreshold = window.outerWidth - window.innerWidth > threshold;
    const heightThreshold = window.outerHeight - window.innerHeight > threshold;
    
    if ((widthThreshold || heightThreshold) && !devtoolsOpen) {
      devtoolsOpen = true;
      blockAccess();
    }
  };

  // Check frequently
  setInterval(checkDevTools, 500);

  // Debugger trap - causes immediate detection if DevTools is open
  setInterval(() => {
    const before = new Date();
    debugger;
    const after = new Date();
    // If debugger statement paused execution, DevTools is open
    if (after - before > 100 && !devtoolsOpen) {
      devtoolsOpen = true;
      blockAccess();
    }
  }, 1000);

  // Advanced DevTools detection using console timing
  let checkCount = 0;
  setInterval(() => {
    const startTime = performance.now();
    console.log('%c', 'color: transparent');
    console.clear();
    const endTime = performance.now();
    
    // If logging takes too long, DevTools is likely open
    if (endTime - startTime > 10 && !devtoolsOpen) {
      checkCount++;
      if (checkCount > 2) {
        devtoolsOpen = true;
        blockAccess();
      }
    } else {
      checkCount = 0;
    }
  }, 500);

  // Disable console functions and detect access attempts
  const noop = function() {};
  if (typeof console !== 'undefined') {
    // Replace console methods to hide output
    ['log', 'debug', 'info', 'warn', 'error', 'dir', 'dirxml', 'trace', 'profile', 'profileEnd', 'table', 'assert', 'count', 'group', 'groupEnd', 'time', 'timeEnd'].forEach(method => {
      try {
        console[method] = noop;
      } catch(e) {}
    });
  }

  // Protect against function inspection
  const originalToString = Function.prototype.toString;
  Function.prototype.toString = function() {
    if (this === blockAccess || this === checkDevTools || this === noop) {
      return 'function() { [native code] }';
    }
    return originalToString.call(this);
  };

  // Add one more detection: Firebug/DevTools check via performance
  (function() {
    const devtools = /./;
    devtools.toString = function() {
      devtoolsOpen = true;
      blockAccess();
    };
    console.log('%c', devtools);
  })();

})();
