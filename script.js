/* ============================================
   CIVICO23 — Scripts
   ============================================ */

(function () {
  'use strict';

  // --- Mobile Menu Toggle ---
  var toggle = document.getElementById('nav-toggle');
  var links = document.getElementById('nav-links');

  toggle.addEventListener('click', function () {
    toggle.classList.toggle('active');
    links.classList.toggle('open');
  });

  // Close menu when a link is clicked
  links.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', function () {
      toggle.classList.remove('active');
      links.classList.remove('open');
    });
  });

  // --- Navbar scroll effect ---
  var nav = document.getElementById('nav');
  window.addEventListener('scroll', function () {
    if (window.scrollY > 50) {
      nav.classList.add('scrolled');
    } else {
      nav.classList.remove('scrolled');
    }
  });

  // --- Scroll Reveal ---
  var revealElements = document.querySelectorAll(
    '.chi-siamo-content, .band-card, .timeline-item, .album-showcase, .evento-card, .contatti-content'
  );

  revealElements.forEach(function (el) {
    el.classList.add('reveal');
  });

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
  );

  revealElements.forEach(function (el) {
    observer.observe(el);
  });

  // --- Stagger band cards animation ---
  var bandCards = document.querySelectorAll('.band-card');
  bandCards.forEach(function (card, i) {
    card.style.transitionDelay = (i * 0.1) + 's';
  });

  // --- Band photo highlight on card hover ---
  var bandPhoto = document.getElementById('band-photo');
  if (bandPhoto) {
    bandCards.forEach(function (card) {
      var member = card.getAttribute('data-member');
      if (!member) return;
      card.addEventListener('mouseenter', function () {
        bandPhoto.className = 'band-photo highlight-' + member;
      });
      card.addEventListener('mouseleave', function () {
        bandPhoto.className = 'band-photo';
      });
    });
  }

  // --- Stagger timeline items ---
  var timelineItems = document.querySelectorAll('.timeline-item');
  timelineItems.forEach(function (item, i) {
    item.style.transitionDelay = (i * 0.15) + 's';
  });

  // --- Stagger event cards ---
  var eventoCards = document.querySelectorAll('.evento-card');
  eventoCards.forEach(function (card, i) {
    card.style.transitionDelay = (i * 0.1) + 's';
  });
})();
