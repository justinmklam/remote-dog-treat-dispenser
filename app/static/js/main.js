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
        console.log("give treat")
        fetch(App.routes.giveTreat, {method: "POST"});
    }
}

window.addEventListener("load", function () {
    App.init();
});
