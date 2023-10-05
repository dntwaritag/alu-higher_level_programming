$(document).ready(function() {
  $('INPUT#btn_translate').click(fetchTranslation);
  $('INPUT#language_code').keydown(function(event) {
    if (event.keyCode === 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation() {
    const languageCode = $('INPUT#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;

    $.get(url, function(data) {
      $('DIV#hello').text(data.hello);
    });
  }
