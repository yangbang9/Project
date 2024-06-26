$(document).ready(function () {
  // 선수 이름을 자동완성하기 위한 배열
  var playerNames = [];

  // jQuery UI Autocomplete 설정
  $('#player_name').autocomplete({
      source: function (request, response) {
          var results = $.ui.autocomplete.filter(playerNames, request.term);
          response(results.slice(0, 10)); // 최대 10개의 결과를 표시
      }
  });

  // 선수 이름 배열을 서버에서 가져옴 (자동완성 데이터)
  $.get('/autocomplete-players/', function (data) {
      playerNames = data;
  });
});
