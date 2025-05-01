<script lang="ts">
  import { onMount } from 'svelte';

  let today = '';
  let articles: any[] = [];
  let articlesWithImages: any[] = [];
  let error = '';

  function getImage(article: any): string | null {
    if (article?.multimedia?.default?.url) {
      return article.multimedia.default.url;
    } else if (article?.multimedia?.thumbnail?.url) {
      return article.multimedia.thumbnail.url;
    }
    return null;
  }

  onMount(async () => {
    const now = new Date();
    today = now.toLocaleDateString('en-US', {
      weekday: 'long',
      month: 'long',
      day: 'numeric',
      year: 'numeric',
    });

    try {
      const res = await fetch('http://localhost:8000/api/local-news');
      const data = await res.json();
      articles = data.response?.docs || [];
      articlesWithImages = articles.filter(article => getImage(article));
      console.log("Filtered image-backed articles:", articlesWithImages);
    } catch (e) {
      error = 'Failed to load articles';
      console.error(e);
    }
  });
</script>

<main>
  <header>
    <div class="date">
      <p><b>{today}</b><br /> Today’s Paper</p>
      <br />
    </div>
    <div class="logo-image">
      <img src="/NYTimeslogo.png" alt="The New York Times" />
    </div>
    <hr style="margin: 1% 2% 1% 2%; width: 95%" />
  </header>

  {#if articlesWithImages.length > 0}
    <div class="main-container">
      <!-- Left Column -->
      <div class="left-column">
        {#each articlesWithImages.slice(1, 3) as article}
          <h2>{article.headline.main}</h2>
          <p>{article.abstract}</p>
          <img src={getImage(article)} alt={article.headline.main} width="100%" />
          <p>{article.lead_paragraph}</p>
          <hr />
        {/each}
      </div>

      <!-- Mid Column -->
      <div class="mid-column">
        <h1>{articlesWithImages[0].headline.main}</h1>
        <p>{articlesWithImages[0].abstract}</p>
        <img src={getImage(articlesWithImages[0])} alt={articlesWithImages[0].headline.main} width="100%" />
        <p>{articlesWithImages[0].lead_paragraph}</p>
        <hr />

        {#if articlesWithImages[3]}
          <h3>{articlesWithImages[3].headline.main}</h3>
          <p>{articlesWithImages[3].abstract}</p>
          <img src={getImage(articlesWithImages[3])} alt={articlesWithImages[3].headline.main} width="100%" />
          <p>{articlesWithImages[3].lead_paragraph}</p>
        {/if}
      </div>

      <!-- Right Column -->
      <div class="right-column">
        {#each articlesWithImages.slice(4, 6) as article}
          <h2>{article.headline.main}</h2>
          <p>{article.abstract}</p>
          <img src={getImage(article)} alt={article.headline.main} width="100%" />
          <p>{article.lead_paragraph}</p>
          <hr />
        {/each}
      </div>
    </div>
  {:else}
    <p>Loading articles with images or not enough content available...</p>
  {/if}

  <hr style="height: 3px; background-color: black; margin: 2% 2% 3% 2%" />
</main>

<!-- <script lang="ts">
  import { onMount } from 'svelte';

  let today = '';
  let articles: any[] = [];

  onMount(async () => {
    const now = new Date();
    today = now.toLocaleDateString('en-US', {
      weekday: 'long',
      month: 'long',
      day: 'numeric',
      year: 'numeric',
    });

    try {
      const res = await fetch('http://localhost:8000/api/local-news');
      const data = await res.json();
      articles = data.response?.docs || [];
    } catch (e) {
      console.error('Failed to fetch NYT articles:', e);
    }
  });

    function getImage(article: any): string | null {
    if (article?.multimedia && article.multimedia.length > 0) {
      const image = article.multimedia.find((m: any) => m.subtype === 'superJumbo') || article.multimedia[0];
      console.log("Image URL for article:", url);  
      console.log("Full article[2]:", articles[2]);
      console.log("hello");
      return "https://static01.nyt.com/" + image.url;
    }
    return null;
}
</script>





<main>
  <header>
    <div class="date">
      <p><b>{today}</b><br /> Today’s Paper</p>
      <br />
    </div>
    <div class="logo-image">
      <img src="/NYTimeslogo.png" alt="The New York Times" />
    </div>
    <hr style="margin: 1% 2% 1% 2%; width: 95%" />
  </header>

  {#if articles.length > 5}
    <div class="main-container">
      <div class="left-column">
        <h2>{articles[2].headline.main}</h2>
        <p>{articles[2].abstract}</p>
        {#if getImage(articles[2])}
          <img src={getImage(articles[2])} alt={articles[2].headline?.main} width="100%" />
        {/if}

        <hr />
        <p>{articles[2].lead_paragraph}</p>

        <h2>{articles[3].headline.main}</h2>
        <p>{articles[3].abstract}</p>
        {#if getImage(articles[3])}
        <img src={getImage(articles[3])} alt={articles[3].headline?.main} width="100%" />
      {/if}
        <p>{articles[3].lead_paragraph}</p>
      </div>

      <div class="mid-column">
        <h1>{articles[0].headline.main}</h1>
        <p>{articles[0].abstract}</p>
        {#if articles[0].multimedia?.length}
          <img
            src={"https://static01.nyt.com/" + articles[0].multimedia[0].url}
            alt={articles[0].headline.main}
          />
        {/if}
        <hr />
        <p>{articles[0].lead_paragraph}</p>

        <h3>{articles[1].headline.main}</h3>
        <p>{articles[1].abstract}</p>
        {#if articles[1].multimedia?.length}
          <img
            src={"https://static01.nyt.com/" + articles[1].multimedia[0].url}
            alt={articles[1].headline.main}
          />
        {/if}
        <p>{articles[1].lead_paragraph}</p>
      </div>

      <div class="right-column">
        <h2>{articles[4].headline.main}</h2>
        <p>{articles[4].abstract}</p>
        {#if articles[4].multimedia?.length}
          <img
            src={"https://static01.nyt.com/" + articles[4].multimedia[0].url}
            alt={articles[4].headline.main}
          />
        {/if}
        <hr />
        <p>{articles[4].lead_paragraph}</p>

        <h2>{articles[5].headline.main}</h2>
        <p>{articles[5].abstract}</p>
        {#if articles[5].multimedia?.length}
          <img
            src={"https://static01.nyt.com/" + articles[5].multimedia[0].url}
            alt={articles[5].headline.main}
          />
        {/if}
        <p>{articles[5].lead_paragraph}</p>
      </div>
    </div>
  {:else}
    <p>Loading articles or not enough articles yet...</p>
  {/if}

  <hr style="height: 3px; background-color: black; margin: 2% 2% 3% 2%" />
</main>

 -->
