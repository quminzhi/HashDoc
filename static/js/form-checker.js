// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
    "use strict";
    window.addEventListener(
        "load",
        function () {
            // Fetch all the forms we want to apply custom Bootstrap validation styles to
            var forms = document.getElementsByClassName("needs-validation");

            // Loop over them and prevent submission
            Array.prototype.filter.call(forms, function (form) {
                form.addEventListener(
                    "submit",
                    function (event) {
                        if (form.checkValidity() === false) {
                            event.preventDefault();
                            event.stopPropagation();
                        }
                        else {
                            let btn = document.getElementById("submit-btn");
                            btn.setAttribute("disabled", true);
                            btn.innerHTML = `
                            <span class="spinner-grow spinner-grow-sm" style="width: 1.2rem; height: 1.2rem;" role="status" aria-hidden="true"></span>
                            Process
                            `
                        }
                        form.classList.add("was-validated");
                    },
                    false
                );
            });
        },
        false
    );
})();
