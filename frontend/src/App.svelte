<script lang="ts">
  import { onMount } from 'svelte';

  let today = '';
  let articles: any[] = [];
  let imageArticles: any[] = [];
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
      imageArticles = articles.filter(article => getImage(article));
      console.log("Filtered image-backed articles:", imageArticles);
    } catch (e) {
      error = 'Failed to load articles';
      console.error(e);
    }
  });
</script>

<main>
  <header>
    <div class="date">
      <p><b>{today}</b><br/> Today’s Paper</p>
      <br />
    </div>
    <div class="logo-image">
      <img src="/NYTimeslogo.png" alt="The New York Times" />
    </div>
    <hr style="margin: 1% 2% 2% 2%; width: 95%" />
  </header>

  {#if imageArticles.length > 0}
    <div class="main-container">
      <div class="left-column">
        {#each imageArticles.slice(2, 4) as article}
          <img src={getImage(article)} alt={article.headline.main}/>
          <h2>{article.headline.main}</h2>
          <p>{article.abstract}</p>
          <p>{article.lead_paragraph}</p>
          <hr/>
        {/each}
      </div>

      <div class="mid-column">
        <img src={getImage(imageArticles[0])} alt={imageArticles[0].headline.main}/>
        <h1>{imageArticles[0].headline.main}</h1>
        <p>{imageArticles[0].abstract}</p>
        <p>{imageArticles[0].lead_paragraph}</p>
        <hr style="margin: 1% 0% 5% 0%"/>

        {#if imageArticles[1]}
          <img src={getImage(imageArticles[1])} alt={imageArticles[1].headline.main}/>
          <h3>{imageArticles[1].headline.main}</h3>
          <p>{imageArticles[1].abstract}</p>
          <p>{imageArticles[1].lead_paragraph}</p>
        {/if}
      </div>

      <div class="right-column">
        <img src={getImage(imageArticles[5])} alt={imageArticles[5].headline.main}/>
        <h2>{imageArticles[5].headline.main}</h2>
        <p>{imageArticles[5].abstract}</p>
        <p>{imageArticles[5].lead_paragraph}</p>
        <hr style="margin: 5% 0% 10% 0%"/>

        {#if imageArticles[7]}
          <img src={getImage(imageArticles[7])} alt={imageArticles[7].headline.main}/>
          <h2>{imageArticles[7].headline.main}</h2>
          <p>{imageArticles[7].abstract}</p>
          <p>{imageArticles[7].lead_paragraph}</p>
        {/if}
      </div>

      <div class="side-columns">
        {#each imageArticles.slice(2, 4) as article}
          <img src={getImage(article)} alt={article.headline.main}/>
          <h2>{article.headline.main}</h2>
          <p>{article.abstract}</p>
          <p>{article.lead_paragraph}</p>
          <hr />
        {/each}

        <img src={getImage(imageArticles[5])} alt={imageArticles[5].headline.main}/>
        <h2>{imageArticles[5].headline.main}</h2>
        <p>{imageArticles[5].abstract}</p>
        <p>{imageArticles[5].lead_paragraph}</p>
        <hr style="margin: 5% 0% 10% 0%"/>

        {#if imageArticles[7]}
          <img src={getImage(imageArticles[7])} alt={imageArticles[7].headline.main}/>
          <h2>{imageArticles[7].headline.main}</h2>
          <p>{imageArticles[7].abstract}</p>
          <p>{imageArticles[7].lead_paragraph}</p>
        {/if}
        <hr/>
      </div>
    </div>
  {:else}
    <p>Loading articles with images or not enough content available...</p>
  {/if}
  <hr style="height: 3px; background-color: black; margin: 2% 2% 3% 2%" />
</main> 

