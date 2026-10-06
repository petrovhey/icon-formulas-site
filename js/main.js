(function () {
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.querySelector(".nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  document.querySelectorAll(".faq-item").forEach(function (item) {
    var btn = item.querySelector("button");
    if (!btn) return;
    btn.addEventListener("click", function () {
      var isOpen = item.hasAttribute("open");
      document.querySelectorAll(".faq-item[open]").forEach(function (other) {
        other.removeAttribute("open");
        var ob = other.querySelector("button");
        if (ob) ob.setAttribute("aria-expanded", "false");
      });
      if (!isOpen) {
        item.setAttribute("open", "");
        btn.setAttribute("aria-expanded", "true");
      }
    });
  });

  var mainImg = document.querySelector(".pdp-main img");
  var thumbs = document.querySelectorAll(".pdp-thumbs button");
  if (mainImg && thumbs.length) {
    thumbs.forEach(function (thumb) {
      thumb.addEventListener("click", function () {
        var src = thumb.getAttribute("data-full") || thumb.querySelector("img")?.src;
        if (src) mainImg.src = src;
        thumbs.forEach(function (t) {
          t.setAttribute("aria-selected", t === thumb ? "true" : "false");
        });
      });
    });
  }
})();
