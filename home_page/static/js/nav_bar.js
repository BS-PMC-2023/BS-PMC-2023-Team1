var navItems = [];

/* JS for navbar transition effect when toggle up / down the page */
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.nav-bar');
    const dropbox = document.querySelector('.select-box-list');
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTop > 220) {
        navbar.classList.remove('slide-up');
        navbar.classList.add('slide-down');
        dropbox.classList.remove('dropbox-unshadowed');
        dropbox.classList.add('dropbox-shadowed');
        navItems.forEach(function(navItem) {
            navItem.style.marginBottom = '0';
        });
    }
    else {
        navbar.classList.remove('slide-down');
        navbar.classList.add('slide-up');
        dropbox.classList.remove('dropbox-shadowed');
        dropbox.classList.add('dropbox-unshadowed');
        navItems.forEach(function(navItem) {
            navItem.style.marginBottom = '-4px';
        });
    }
});


/* JS for navbar items. It will keep the underline constantly after clicking on some item */
window.onload = function() {
    var currentUrl = window.location.href;
    navItems = [
        document.querySelector('.nav-item1'),
        document.querySelector('.nav-item2'),
        document.querySelector('.nav-item3'),
        document.querySelector('.nav-item4'),
        document.querySelector('.nav-item5'),
        document.querySelector('.nav-item6'),
        document.querySelector('.nav-item7'),
        document.querySelector('.nav-item8'),
        document.querySelector('.nav-item9')
    ];

    if (currentUrl.includes('users')) {
        navItems[0].classList.add('clicked');
    }
    if (currentUrl.includes('myProfile')) {
         navItems[1].classList.add('clicked');
    }
    if (currentUrl.includes('myarticle')) {
         navItems[2].classList.add('clicked');
    }
    if (currentUrl.includes('favoriteExpert')) {
        if (currentUrl.includes('favoriteArticle')) {
             navItems[4].classList.add('clicked');
        } else {
             navItems[3].classList.add('clicked');
        }
    }
    if (currentUrl.includes('articles')) {
         navItems[5].classList.add('clicked');
    }
    if (currentUrl.includes('register')) {
         navItems[6].classList.add('clicked');
    }
    if (currentUrl.includes('login')) {
         navItems[7].classList.add('clicked');
    }
    if (currentUrl.includes('reviews')) {
         navItems[8].classList.add('clicked');
    }
};
