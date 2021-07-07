$("#steps").steps({
    headerTag: "h3",
    bodyTag: "section",
    transitionEffect: "slideLeft",
    autoFocus: true,
    onFinished: () => {
        window.location.href = nextURL;
    },
    labels:{
        previous: gettext('Anterior'),
        next: gettext('Siguiente'),
        finish: gettext('Finalizar'),
    }
});