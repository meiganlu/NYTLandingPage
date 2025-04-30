<script lang="ts">
  import { onMount } from 'svelte';

  let today = '';
  let articles: any[] = [];

  onMount(async () => {
    // Format date
    const now = new Date();
    today = now.toLocaleDateString('en-US', {
      weekday: 'long',
      month: 'long',
      day: 'numeric',
      year: 'numeric',
    });

    // Fetch articles from backend
    try {
      const res = await fetch('/api/local-news');
      const data = await res.json();
      articles = data.response.docs;
    } catch (e) {
      console.error('Failed to fetch NYT articles:', e);
    }
  });
</script>

<main>
  <header>
    <div class="date">
      <p>
        <b>{today}</b><br />
        Today’s Paper
      </p>
      <br>
    </div>
    <div class="logo-image">
      <img src="/NYTimeslogo.png" alt="The New York Times logo" />
    </div>
    <hr style="margin: 1% 2% 1% 2%; width: 95%" />
  </header>

  <div class="main-container">
    <!-- Mid column: show first story -->
    <div class="mid-column">
      {#if articles.length > 0}
        <h1><a href={articles[0].web_url} target="_blank">{articles[0].headline.main}</a></h1>
        <p>{articles[0].abstract || articles[0].lead_paragraph}</p>
        <hr />
      {/if}
    </div>
  
    <!-- Left column: next few stories -->
    <div class="left-column">
      {#each articles.slice(1, 4) as article}
        <h2><a href={article.web_url} target="_blank">{article.headline.main}</a></h2>
        <p>{article.abstract || article.lead_paragraph}</p>
        <hr />
      {/each}
    </div>
  
    <!-- Right column: more stories -->
    <div class="right-column">
      {#each articles.slice(1, 4) as article}
        <div class="story">
          {#if article.multimedia && article.multimedia.length > 0}
            <img src={"https://static01.nyt.com/" + article.multimedia[0].url} alt="article" width="100%" />
          {/if}
          <h2><a href={article.web_url} target="_blank">{article.headline.main}</a></h2>
          <p>{article.abstract || article.lead_paragraph}</p>
          <hr />
        </div>
      {/each}
    </div>
  </div>  

  <hr style="height: 3px; background-color: black; margin: 2% 2% 3% 2%" />
</main>
