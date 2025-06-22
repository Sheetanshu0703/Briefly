// Enhanced interactions and animations
document.addEventListener('DOMContentLoaded', function() {
    // Add particle effect
    createParticles();
    
    // Add typing effect to header
    const headerText = document.querySelector('.header h1');
    if (headerText) {
        headerText.classList.add('typing-effect');
    }
    
    // Add floating animation to logo
    const logo = document.querySelector('.logo');
    if (logo) {
        logo.classList.add('floating');
    }
    
    // Add glow effect to buttons
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(btn => {
        btn.classList.add('glow-effect');
    });
    
    // Add character counter
    const textarea = document.getElementById('textInput');
    if (textarea) {
        const counter = document.createElement('div');
        counter.id = 'charCounter';
        counter.style.cssText = 'text-align: right; font-size: 0.8rem; color: #666; margin-top: 5px;';
        textarea.parentNode.appendChild(counter);
        
        textarea.addEventListener('input', function() {
            const count = this.value.length;
            counter.textContent = `${count} characters`;
            
            if (count >= 50) {
                counter.style.color = '#28a745';
            } else if (count > 0) {
                counter.style.color = '#ffc107';
            } else {
                counter.style.color = '#666';
            }
        });
    }
});

function createParticles() {
    const container = document.body;
    const particleCount = 20;
    
    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.left = Math.random() * 100 + 'vw';
        particle.style.animationDelay = Math.random() * 6 + 's';
        particle.style.animationDuration = (Math.random() * 3 + 3) + 's';
        container.appendChild(particle);
    }
}

// Enhanced form submission with better UX
function enhanceFormSubmission() {
    const form = document.getElementById('summarizeForm');
    const submitBtn = document.getElementById('submitBtn');
    const loading = document.getElementById('loading');
    const result = document.getElementById('result');
    const error = document.getElementById('error');
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const textInput = document.getElementById('textInput').value.trim();
        if (textInput.length < 50) {
            showNotification('Please enter at least 50 characters for summarization.', 'warning');
            return;
        }
        
        // Show loading with enhanced animation
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
        loading.style.display = 'block';
        result.style.display = 'none';
        error.style.display = 'none';
        
        try {
            const formData = new FormData();
            formData.append('text', textInput);
            
            const response = await fetch('/predict', {
                method: 'POST',
                body: formData
            });
            
            const data = await response.json();
            
            if (data.status === 'success') {
                // Update results with animation
                updateResults(data);
                result.style.display = 'block';
                result.classList.add('success-animation');
                
                // Remove animation class after animation completes
                setTimeout(() => {
                    result.classList.remove('success-animation');
                }, 600);
                
                showNotification('Summary generated successfully!', 'success');
            } else {
                throw new Error(data.message);
            }
        } catch (err) {
            error.textContent = `Error: ${err.message}`;
            error.style.display = 'block';
            showNotification('Failed to generate summary. Please try again.', 'error');
        } finally {
            submitBtn.disabled = false;
            submitBtn.innerHTML = '<i class="fas fa-magic"></i> Generate Summary';
            loading.style.display = 'none';
        }
    });
}

function updateResults(data) {
    document.getElementById('summaryText').innerHTML = `
        <p><strong>Original Text:</strong></p>
        <p style="background: #f8f9fa; padding: 15px; border-radius: 8px; margin-bottom: 15px; max-height: 150px; overflow-y: auto;">
            ${data.original_text.substring(0, 200)}${data.original_text.length > 200 ? '...' : ''}
        </p>
        <p><strong>Summary:</strong></p>
        <p style="background: #e8f5e8; padding: 15px; border-radius: 8px; border-left: 4px solid #28a745;">
            ${data.summary}
        </p>
    `;
    
    // Animate statistics
    animateCounter('originalLength', data.original_length);
    animateCounter('summaryLength', data.summary_length);
    animateCounter('compressionRatio', data.compression_ratio, '%');
}

function animateCounter(elementId, targetValue, suffix = '') {
    const element = document.getElementById(elementId);
    const startValue = 0;
    const duration = 1000;
    const startTime = performance.now();
    
    function updateCounter(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        const currentValue = Math.floor(startValue + (targetValue - startValue) * progress);
        element.textContent = currentValue + suffix;
        
        if (progress < 1) {
            requestAnimationFrame(updateCounter);
        }
    }
    
    requestAnimationFrame(updateCounter);
}

function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        padding: 15px 20px;
        border-radius: 8px;
        color: white;
        font-weight: 600;
        z-index: 1000;
        transform: translateX(100%);
        transition: transform 0.3s ease;
        max-width: 300px;
    `;
    
    // Set background color based on type
    switch(type) {
        case 'success':
            notification.style.background = '#28a745';
            break;
        case 'error':
            notification.style.background = '#dc3545';
            break;
        case 'warning':
            notification.style.background = '#ffc107';
            notification.style.color = '#333';
            break;
        default:
            notification.style.background = '#17a2b8';
    }
    
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Remove after 5 seconds
    setTimeout(() => {
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            document.body.removeChild(notification);
        }, 300);
    }, 5000);
}

// Initialize enhanced form submission
enhanceFormSubmission(); 