<script>
 var bigBg = document.querySelector("header .fixed.top");
      var burger = document.querySelector(".cmpt-nav .icon-menu-charcoal");
      var button = document.querySelector(".cmpt-nav &gt; div");

      var closeButton = document.querySelector(
        ".main-nav-dropdown__close-button"
      );
      var mainNav = document.querySelector(".cmpt-nav");
      var mainDropdown = document.querySelector(".js-main-nav-dropdown");
      var dropdownSubsections = document.querySelectorAll(
        ".main-nav-dropdown__subsection"
      );
      var mainDropdownItem = document.querySelectorAll(
        ".main-nav-dropdown__item-control"
      );
      var reportButton = document.querySelector(".cmpt-nav &gt; .xlarge-up-flex");
      var reportContent = document.querySelector(
        ".cmpt-nav &gt; .xlarge-up-flex .bg-white"
      );
      var mainSectionsArray = 
Array.prototype.slice.call
(mainDropdownItem);
      var subsectionsArray = 
Array.prototype.slice.call
(dropdownSubsections);

      function startDropdown() {
        if (window.innerWidth &lt; 751) {
          burger.addEventListener("click", function () {
            mainDropdown.classList.add("is-open", "has-visibile-subsection");
          });

          closeButton.addEventListener("click", function () {
            mainDropdown.classList.remove("is-open");
          });

          
mainSectionsArray.map
(function (section) {
            section.addEventListener("click", function (e) {
              e.preventDefault();
              console.log("click");

              var sectionData = section.getAttribute("data-detail");
              var sectionId = JSON.parse(sectionData).childListId;
              //Clear state
              mainDropdown.classList.remove("has-visibile-subsection");
              
subsectionsArray.map
(function (item) {
                item.setAttribute("hidden", "");
                item.classList.add("is-selected");
              });

              mainDropdown.classList.add("has-visibile-subsection");

              
subsectionsArray.map
(function (item) {
                var subSectionId = item.getAttribute("data-list-id");
                if (sectionId === subSectionId) {
                  item.removeAttribute("hidden");
                }
              });
            });
          });
        } else {
          button.addEventListener("mouseover", function () {
            mainDropdown.classList.add("is-open");
            bigBg.classList.remove("animate-fade-hidden");
            bigBg.classList.add("animate-fade-entered");
          });

          mainNav.addEventListener("mouseout", function () {
            mainDropdown.classList.remove("is-open");
            bigBg.classList.add("animate-fade-hidden");
            bigBg.classList.remove("animate-fade-entered");
          });

          
mainSectionsArray.map
(function (section) {
            section.addEventListener("mouseover", function () {
              var sectionData = section.getAttribute("data-detail");
              var sectionId = JSON.parse(sectionData).childListId;
              //Clear state
              mainDropdown.classList.remove("has-visibile-subsection");
              
subsectionsArray.map
(function (item) {
                item.setAttribute("hidden", "");
              });

              mainDropdown.classList.add("has-visibile-subsection");

              
subsectionsArray.map
(function (item) {
                var subSectionId = item.getAttribute("data-list-id");
                if (sectionId === subSectionId) {
                  item.removeAttribute("hidden");
                }
              });
            });
          });

          reportButton.addEventListener("mouseover", function () {
            reportContent.classList.remove("animate-fade-hidden");
            reportContent.classList.add("animate-fade-entered");
            bigBg.classList.remove("animate-fade-hidden");
            bigBg.classList.add("animate-fade-entered");
          });

          reportButton.addEventListener("mouseout", function () {
            reportContent.classList.remove("animate-fade-entered");
            reportContent.classList.add("animate-fade-hidden");
            bigBg.classList.add("animate-fade-hidden");
            bigBg.classList.remove("animate-fade-entered");
          });
        }
      }

      startDropdown();

      window.addEventListener("resize", (event) =&gt; {
        startDropdown();
      });
</script>
