document.addEventListener("DOMContentLoaded", function () {
    // Function to handle hover for desktop
    function handleHover() {
        document.querySelectorAll('.dropdown-menu > .nav-item').forEach(function (item) {
            item.addEventListener('mouseover', function () {
                this.classList.add('hover');
            });
            item.addEventListener('mouseout', function () {
                this.classList.remove('hover');
            });
        });
    }

    // Function to handle click for mobile
    function handleClick() {
        document.querySelectorAll('.dropdown-menu a').forEach(function (element) {
            element.addEventListener('click', function (e) {
                let nextEl = this.nextElementSibling;
                if (nextEl && nextEl.classList.contains('submenu')) {
                    e.preventDefault();
                    if (nextEl.style.display == 'block') {
                        nextEl.style.display = 'none';
                    } else {
                        nextEl.style.display = 'block';
                    }
                }
            });

            // Handle touch events
            element.addEventListener('touchstart', function (e) {
                let nextEl = this.nextElementSibling;
                if (nextEl && nextEl.classList.contains('submenu')) {
                    e.preventDefault();
                    if (nextEl.style.display == 'block') {
                        nextEl.style.display = 'none';
                    } else {
                        nextEl.style.display = 'block';
                    }
                }
            });
        });
    }

    // Initial load
    handleHover();
    handleClick();

    // Refresh functions on window resize
    window.addEventListener('resize', function () {
        removeEventListener()
        handleHover();
        handleClick();
    });
});



// ======= navbar text color change ========

// document.addEventListener('DOMContentLoaded', function () {
//     let navbar = document.querySelector('.navbar');

//     if (navbar) {
//         const toggleNavbarBackground = () => {
//             if (window.scrollY > 800) {
//                 navbar.classList.add('scrolled');
//             } else {
//                 navbar.classList.remove('scrolled');
//             }
//         };

//         window.addEventListener('scroll', toggleNavbarBackground);
//         toggleNavbarBackground(); // Call initially to set initial state

//     }
// });


// ======== Back to top button ============

// document.addEventListener('DOMContentLoaded', function () {
//     let backtotop = document.querySelector('.back-to-top');

//     if (backtotop) {
//         const toggleBacktotop = () => {
//             if (window.scrollY > 100) {
//                 backtotop.classList.add('active');
//             } else {
//                 backtotop.classList.remove('active');
//             }
//         };

//         window.addEventListener('scroll', toggleBacktotop);
//         toggleBacktotop(); // Call initially to set initial state

//         // Smooth scroll to top on button click
//         backtotop.addEventListener('click', function (e) {
//             e.preventDefault();
//             window.scrollTo({ top: 0, behavior: 'smooth' });
//         });
//     }
// });

 /**
   * Preloader
   */
 document.addEventListener('DOMContentLoaded', () => {
    const preloader = document.querySelector('#preloader');
    
    if (preloader) {
      // Wait until the entire page is fully loaded (images, iframes, etc.)
      window.addEventListener('load', () => {
        // Apply a transition effect to fade out the preloader
        preloader.style.transition = 'opacity 0.5s ease-out';
        preloader.style.opacity = '0'; // Fade out the preloader
        
        // Remove the preloader after the fade-out transition is complete
        setTimeout(() => {
          preloader.remove();
        }, 500); // Match this delay to the duration of the opacity transition
      });
    }
  });

// ========== Testimonial slider ===========
// $(document).ready(function () {
//     pagenum = 1;
//     function AutoRotate() {
//         var myele = null;
//         var allElements = document.getElementsByTagName('label');
//         for (var i = 0, n = allElements.length; i < n; i++) {
//             var myfor = allElements[i].getAttribute('for');
//             if ((myfor !== null) && (myfor == ('slide_2_' + pagenum))) {
//                 allElements[i].click();
//                 break;
//             }
//         }
//         if (pagenum == 4) {
//             pagenum = 1;
//         } else {
//             pagenum++;
//         }
//     }
//     setInterval(AutoRotate, 5000);
// });