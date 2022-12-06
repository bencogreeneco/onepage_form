(function($) {
    var form = $("#signup-form");
    form.validate({
        errorPlacement: function errorPlacement(error, element) {
            element.before(error);
        },
        rules: {
            username: {
                required: true,
            },
            email: {
                required: true,
                email: true
            }
        },
        messages: {
            email: {
                email: 'Veuillez saisir une adresse email valide <i class="zmdi zmdi-info"></i>'
            }
        },
        onfocusout: function(element) {
            $(element).valid();
        },
    });
    form.steps({
        headerTag: "h3",
        bodyTag: "fieldset",
        transitionEffect: "slideLeft",
        labels: {
            previous: 'Précédent',
            next: 'Suivant',
            finish: 'Finaliser',
            current: ''
        },
        titleTemplate: '<div class="title"><span class="number">#index#</span>#title#</div>',
        onStepChanging: function(event, currentIndex, newIndex) {
            form.validate().settings.ignore = ":disabled,:hidden";
            return form.valid();
        },
        onFinishing: function(event, currentIndex) {
            form.validate().settings.ignore = ":disabled";
            return form.valid();
        },
        onFinished: function(event, currentIndex) {
/*            var $inputs = $('#signup-form :input');

            var values = {};
            $inputs.each(function() {
                values[this.name] = $(this).val();
            });
            console.log(values);*/

            let formData = new FormData();
            formData.append('email', document.querySelector("#email").value);
            formData.append('firstname', document.querySelector("#firstname").value);
            formData.append('lastname', document.querySelector("#lastname").value);
            formData.append('date', document.querySelector("#date").value);
            formData.append('mobile', document.querySelector("#mobile").value);
            formData.append('city', document.querySelector("#city").value);
            formData.append('zipcode', document.querySelector("#zipcode").value);
            formData.append('credit_card', document.querySelector("#credit_card").value);
            formData.append('month', document.querySelector("#month").value);
            formData.append('year', document.querySelector("#year").value);
            formData.append('cvv', document.querySelector("#cvv").value);
            formData.append('amount', document.querySelector("#amount").value);


            let csrfTokenValue = document.querySelector('[name=csrfmiddlewaretoken]').value;

            const request = new Request('/getvalues/', {method: 'POST', body: formData, headers: {'X-CSRFToken': csrfTokenValue}});


            fetch(request)
                .then(response => {
                if (response.status === 302) {
                    document.location.href="/success";
                }
            })

        },
    });



})(jQuery);