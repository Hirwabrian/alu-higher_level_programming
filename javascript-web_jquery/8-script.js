$.get('https://swapi.dev/api/films/?format=json', function (data) {
  const ul = $('UL#list_movies');
  data.results.forEach(movie => {
    ul.append(`<li>${movie.title}</li>`);
  });
});
