/* JS for navbar transition effect when toggle up / down the page */
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.nav-bar');
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTop > 220) {
        navbar.classList.remove('slide-up');
        navbar.classList.add('slide-down');
    }
    else {
        navbar.classList.remove('slide-down');
        navbar.classList.add('slide-up');
    }
});
