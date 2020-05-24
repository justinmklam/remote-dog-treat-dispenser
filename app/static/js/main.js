"use strict";

var App = {
    components: {
        btnGiveTreat: document.getElementById("btn-give-treat")
    },

    routes: {
        giveTreat: "give_treat"
    },

    init: function () {
        App.addEventListeners();
    },

    addEventListeners: function () {
        console.log("event listeners")
        App.components.btnGiveTreat.addEventListener("click", App.onGiveTreatClicked);
    },

    onGiveTreatClicked: function () {
        App.components.btnGiveTreat.classList.add("loading");
        setTimeout(function() {
            App.components.btnGiveTreat.classList.remove("loading");
        }, 1000);

        console.log("give treat")
        fetch(App.routes.giveTreat, {method: "POST"});
    }
}

window.addEventListener("DOMContentLoaded", function () {
    App.init();
});
