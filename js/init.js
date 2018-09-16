(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('.parallax').parallax();

  }); // end of document ready
})(jQuery); // end of jQuery name space

// $(document).ready(function(){
//   $('#content').pushpin({
//     top: $('#content').offset().top
//   });
//   $('.scrollspy').scrollSpy({
//     scrollOffset: 0
//   });
// });

document.addEventListener('DOMContentLoaded', function () {
  // var sliderinstance = M.Slider.init(document.querySelectorAll('.slider'));
  // init scrollspy

  // init tabs
  var instance = M.Tabs.init(document.querySelectorAll('.tabs'));
  // initialize collapsible
  var collapsibleInstance = M.Collapsible.init(document.querySelectorAll('.collapsible'));
});
