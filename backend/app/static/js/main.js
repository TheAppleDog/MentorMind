

// ===== SMOOTH SCROLL =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});

// ===== FORM VALIDATION ANIMATIONS =====
const forms = document.querySelectorAll('form');
forms.forEach(form => {
    const inputs = form.querySelectorAll('input, textarea, select');
    
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('fade-in');
        });

        input.addEventListener('invalid', function(e) {
            e.preventDefault();
            this.classList.add('is-invalid');
            this.style.borderColor = '#ef4444';
        });

        input.addEventListener('input', function() {
            if (this.classList.contains('is-invalid')) {
                this.classList.remove('is-invalid');
                this.style.borderColor = '';
            }
        });
    });
});

// ===== TOAST NOTIFICATIONS =====
class Toast {
    static show(message, type = 'success', duration = 3000) {
        const toast = document.createElement('div');
        toast.className = `alert alert-${type} position-fixed`;
        toast.style.cssText = `
            top: 20px;
            right: 20px;
            z-index: 9998;
            min-width: 300px;
            animation: slideInRight 0.3s ease-out;
        `;
        toast.innerHTML = `
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            ${message}
        `;
        
        document.body.appendChild(toast);
        
        const bsAlert = new bootstrap.Alert(toast);
        setTimeout(() => {
            toast.style.animation = 'fadeOut 0.3s ease-out';
            setTimeout(() => bsAlert.close(), 300);
        }, duration);
    }
}

// ===== PAGE TRANSITION LOADING =====
document.addEventListener('click', function(e) {
    const link = e.target.closest('a');
    if (link && link.href && !link.href.includes('#') && 
        !link.target && !e.ctrlKey && !e.metaKey) {
        
        // Check if it's an external link
        if (new URL(link.href).hostname === window.location.hostname) {
            const main = document.querySelector('main');
            if (main) {
                // Removed disabling to prevent UI fade and unclickable elements
            }
        }
    }
});

// Restore opacity when page loads
window.addEventListener('load', function() {
    const main = document.querySelector('main');
    if (main) {
        main.style.opacity = '1';
        main.style.pointerEvents = 'auto';
    }
});

// ===== INTERSECTION OBSERVER FOR FADE-IN =====
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('fade-in');
            observer.unobserve(entry.target);
        }
    });
}, observerOptions);

document.querySelectorAll('.card, .stat-card, .table, .row > div').forEach(el => {
    observer.observe(el);
});

// ===== ANIMATED COUNTERS =====
function animateCounter(element, target, duration = 2000) {
    const start = parseInt(element.textContent) || 0;
    const increment = (target - start) / (duration / 16);
    let current = start;

    const counter = setInterval(() => {
        current += increment;
        if ((increment > 0 && current >= target) || (increment < 0 && current <= target)) {
            element.textContent = target;
            clearInterval(counter);
        } else {
            element.textContent = Math.round(current);
        }
    }, 16);
}

// Trigger counters when they come into view
document.querySelectorAll('[data-counter]').forEach(element => {
    observer.observe(element);
    
    const originalObserverCallback = observer.constructor.prototype.constructor;
    const mutationObserver = new MutationObserver(() => {
        if (element.classList.contains('fade-in')) {
            const target = parseInt(element.dataset.counter);
            animateCounter(element, target);
            mutationObserver.disconnect();
        }
    });
    mutationObserver.observe(element, { attributes: true, attributeFilter: ['class'] });
});

// ===== LOADING SKELETON =====
function showLoadingSkeleton(container) {
    const skeleton = document.createElement('div');
    skeleton.className = 'card placeholder-wave';
    skeleton.innerHTML = `
        <div class="card-body">
            <h5 class="card-title placeholder col-6"></h5>
            <p class="card-text placeholder col-7"></p>
            <p class="card-text placeholder col-8"></p>
        </div>
    `;
    container.appendChild(skeleton);
}

// ===== RIPPLE EFFECT ON BUTTONS =====
document.querySelectorAll('.btn, .card, .dropdown-item').forEach(element => {
    element.addEventListener('click', function(e) {
        const ripple = document.createElement('span');
        const rect = this.getBoundingClientRect();
        const size = Math.min(rect.width, rect.height) * 0.5; // Smaller ripple size
        const x = e.clientX - rect.left - size / 2;
        const y = e.clientY - rect.top - size / 2;

        ripple.style.cssText = `
            position: absolute;
            width: ${size}px;
            height: ${size}px;
            background: rgba(255, 255, 255, 0.15);
            border-radius: 50%;
            left: ${x}px;
            top: ${y}px;
            pointer-events: none;
            animation: ripple 0.6s ease-out;
        `;

        // Add animation if not exists
        if (!document.querySelector('style[data-ripple]')) {
            const style = document.createElement('style');
            style.setAttribute('data-ripple', 'true');
            style.innerHTML = `
                @keyframes ripple {
                    to {
                        transform: scale(2);
                        opacity: 0;
                    }
                }
            `;
            document.head.appendChild(style);
        }

        this.style.position = 'relative';
        this.style.overflow = 'hidden';
        this.appendChild(ripple);
    });
});

// ===== REMOVE RIPPLE SPANS AFTER ANIMATION =====
document.addEventListener("animationend", function (e) {
    if (e.animationName === "ripple") {
        e.target.remove();
    }
});

// ===== CLEAN EXISTING RIPPLE SPANS =====
document.querySelectorAll('[style*="ripple"]').forEach(e => e.remove());

// ===== ACTIVE LINK HIGHLIGHTING =====
function highlightActiveLink() {
    document.querySelectorAll('.nav-link, .nav-item a').forEach(link => {
        link.classList.remove('active');
        if (link.href === window.location.href) {
            link.classList.add('active');
        }
    });
}

highlightActiveLink();
window.addEventListener('hashchange', highlightActiveLink);

// ===== ENSURE BUTTONS ARE ALWAYS CLICKABLE =====
document.addEventListener('DOMContentLoaded', function() {
    // Remove any blocking overlays or modals that prevent clicking
    const style = document.createElement('style');
    style.innerHTML = `
        .btn, button, a.btn, input[type="submit"] {
            pointer-events: auto !important;
            z-index: 10 !important;
            background-filter: none !important;
            -webkit-backdrop-filter: none !important;
            backdrop-filter: none !important;
        }

        /* Remove modal backdrop interference */
        .modal-backdrop {
            display: none !important;
        }

        /* Ensure all interactive elements are clickable */
        a, button, input, select, textarea {
            pointer-events: auto !important;
        }

        /* Disable any blur effects on interaction */
        *:active, *:focus {
            background-filter: none !important;
            -webkit-backdrop-filter: none !important;
            backdrop-filter: none !important;
        }
    `;
    document.head.appendChild(style);

    // Force remove any stuck modal backdrops
    document.querySelectorAll('.modal-backdrop').forEach(el => el.remove());
    document.body.style.overflow = 'auto';
    document.body.style.pointerEvents = 'auto';
});

// ===== SUPER EASY UNIVERSAL FIX FOR WHITE BLURRY EFFECT =====
document.addEventListener('click', () => {
    if (document.activeElement && !['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement.tagName)) {
        document.activeElement.blur();
    }

    // ===== BOOTSTRAP BACKDROP CLEANUP FIX =====
    // Remove Bootstrap classes that cause fade effects
    document.body.classList.remove("modal-open");
    document.querySelectorAll(".modal-backdrop, .offcanvas-backdrop, .dropdown-backdrop")
        .forEach(e => e.remove());

    // ===== MAIN CONTAINER RESET FIX =====
    // Ensure main container is always visible and clickable
    const main = document.querySelector('main');
    if (main) {
        main.style.opacity = '1';
        main.style.pointerEvents = 'auto';
    }
});

// ===== THEME PREFERENCE =====
function initTheme() {
    const isDark = localStorage.getItem('theme') === 'dark' ||
                   window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    if (isDark) {
        document.documentElement.setAttribute('data-theme', 'dark');
    }
}

initTheme();

// ===== FADE OUT ANIMATION =====
const style = document.createElement('style');
style.innerHTML = `
    @keyframes fadeOut {
        to {
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);

console.log('🎉 MentorMind UI enhancements loaded successfully!');

// ===== NOTIFICATION SYSTEM =====
let notificationPollInterval = null;
let lastUnreadCount = 0;

function initNotifications() {
    // Only for logged-in users
    if (!document.querySelector('#notificationBell')) return;

    updateNotificationBadge();
    startNotificationPolling();
    
    // Bell click shows notifications + auto-dismiss
    const bell = document.getElementById('notificationBell');
    if (bell) {
        bell.addEventListener('click', handleNotificationBellClick);
    }
}

function updateNotificationBadge() {
    fetch('/student/api/notifications/unread_count', {
        credentials: 'same-origin'
    })
    .then(response => response.json())
    .then(data => {
        const badge = document.getElementById('notificationBadge');
        const count = data.count || 0;
        if (count > 0) {
            badge.textContent = count > 99 ? '99+' : count;
            badge.style.display = 'block';
        } else {
            badge.style.display = 'none';
        }
        lastUnreadCount = count;
    })
    .catch(err => console.error('Notification badge update failed:', err));
}

function playNotificationSound() {
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    const oscillator = audioContext.createOscillator();
    const gainNode = audioContext.createGain();
    
    oscillator.connect(gainNode);
    gainNode.connect(audioContext.destination);
    
    oscillator.frequency.setValueAtTime(800, audioContext.currentTime);
    oscillator.type = 'sine';
    
    gainNode.gain.setValueAtTime(0.3, audioContext.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.3);
    
    oscillator.start(audioContext.currentTime);
    oscillator.stop(audioContext.currentTime + 0.3);
}

function showNotificationToast(notification) {
    playNotificationSound();
    
    const type = notification.type || 'info';
    const color = type === 'success' ? '#10b981' : 
                  type === 'warning' ? '#f59e0b' : 
                  type === 'error' ? '#ef4444' : '#3b82f6';
    
    Toastify({
        text: notification.title + ': ' + notification.message,
        duration: 5000,
        close: true,
        gravity: "top",
        position: "right",
        backgroundColor: color,
        stopOnFocus: true,
        onClick: () => markAllRead(),
        callback: () => markAllRead()  // On close X also clear all
    }).showToast();
}

function fetchUnreadNotifications() {
    fetch('/student/api/notifications/unread', {
        credentials: 'same-origin'
    })
    .then(response => response.json())
    .then(notifications => {
        notifications.forEach(showNotificationToast);
        updateNotificationBadge();
    })
    .catch(err => console.error('Fetch notifications failed:', err));
}

function markNotificationRead(id) {
    fetch(`/student/api/notifications/read/${id}`, {
        method: 'POST',
        credentials: 'same-origin'
    })
    .then(() => {
        updateNotificationBadge();
    })
.catch(err => console.error('Mark read failed:', err));
}

function markAllRead() {
    fetch('/student/api/notifications/read_all', {
        method: 'POST',
        credentials: 'same-origin'
    })
    .then(response => response.json())
    .then(data => {
        lastUnreadCount = 0;
        updateNotificationBadge();
        console.log('Cleared', data.cleared, 'notifications');
    })
    .catch(err => console.error('Mark all read failed:', err));
}

function handleNotificationBellClick(e) {
    e.preventDefault();
    e.stopPropagation();
    fetchUnreadNotifications();
    // Auto-clear after toasts shown
    setTimeout(markAllRead, 2500);
}

function startNotificationPolling() {
// Poll badge every 10 seconds
    notificationPollInterval = setInterval(() => {
        fetch('/student/api/notifications/unread_count', {
            credentials: 'same-origin'
        })
        .then(response => response.json())
        .then(data => {
            updateNotificationBadge();
        });
    }, 10000);
}

// Stop polling when page unloads
window.addEventListener('beforeunload', () => {
    if (notificationPollInterval) {
        clearInterval(notificationPollInterval);
    }
});

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initNotifications);
} else {
    initNotifications();
}
