/* VERTUS — alpha shared script: nav toggle, gallery lightbox, enquiry form stub,
   reveal-on-scroll. No dependencies. */

(function () {
  "use strict";

  /* Mobile navigation ----------------------------------------------------- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".site-nav");

  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  /* Gallery lightbox ------------------------------------------------------ */
  var galleryLinks = document.querySelectorAll("[data-lightbox]");

  if (galleryLinks.length) {
    var lightbox = document.createElement("div");
    lightbox.className = "lightbox";
    lightbox.setAttribute("role", "dialog");
    lightbox.setAttribute("aria-modal", "true");
    lightbox.setAttribute("aria-label", "Image viewer");
    lightbox.innerHTML =
      '<button class="lightbox__close" type="button" aria-label="Close image viewer">&times;</button>' +
      '<figure style="margin:0"><img src="" alt=""><figcaption class="lightbox__caption"></figcaption></figure>';
    document.body.appendChild(lightbox);

    var lbImg = lightbox.querySelector("img");
    var lbCaption = lightbox.querySelector(".lightbox__caption");
    var lbClose = lightbox.querySelector(".lightbox__close");

    function openLightbox(href, caption) {
      lbImg.src = href;
      lbImg.alt = caption;
      lbCaption.textContent = caption;
      lightbox.classList.add("is-open");
      lbClose.focus();
    }

    function closeLightbox() {
      lightbox.classList.remove("is-open");
      lbImg.src = "";
    }

    galleryLinks.forEach(function (link) {
      link.addEventListener("click", function (e) {
        e.preventDefault();
        openLightbox(link.getAttribute("href"), link.dataset.caption || "");
      });
    });

    lbClose.addEventListener("click", closeLightbox);
    lightbox.addEventListener("click", function (e) {
      if (e.target === lightbox) closeLightbox();
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") closeLightbox();
    });
  }

  /* Enquiry form (alpha stub — wired to a relay service at Live phase) ---- */
  var form = document.querySelector(".enquiry-form");

  if (form) {
    /* Check-out can't be before check-in */
    var checkin = form.querySelector("#checkin");
    var checkout = form.querySelector("#checkout");
    if (checkin && checkout) {
      var today = new Date().toISOString().split("T")[0];
      checkin.min = today;
      checkout.min = today;
      checkin.addEventListener("change", function () {
        checkout.min = checkin.value;
        if (checkout.value && checkout.value < checkin.value) checkout.value = checkin.value;
      });
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var success = document.createElement("p");
      success.className = "form-success";
      success.setAttribute("role", "status");
      success.textContent =
        "Alpha preview: your enquiry was not sent anywhere yet. At the Live phase this form connects to the hotel's inbox via a form relay service.";
      form.replaceWith(success);
      success.scrollIntoView({ behavior: "smooth", block: "center" });
    });
  }

  /* Reveal on scroll (respects prefers-reduced-motion via CSS) ------------ */
  var revealEls = document.querySelectorAll(".reveal");

  if (revealEls.length && "IntersectionObserver" in window) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    revealEls.forEach(function (el) { observer.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("is-visible"); });
  }
})();
