<script lang="ts">
    import { onMount } from 'svelte';
  
    // let apiKey: string = '';
    const apiKey = import.meta.env.NYT_API_KEY;
    let articles: any[] = [];
    let error: string = '';
    let formattedDate: string = ''; 
  
    onMount(async () => {
      const currdate = new Date();
      const options: Intl.DateTimeFormatOptions = {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      };
      formattedDate = currdate.toLocaleDateString('en-US', options);
      
      try {
        // const res = await fetch('/api/key');
        // apiKey = data.apiKey;
        const res = await fetch('/api/key');
        const data = await res.json();
        articles = data.response.docs;
      } catch (error) {
        console.error('Failed to fetch articles: ', error);
      }
    });
</script>

<header>
  <div class="date">
    <p><b>{formattedDate}</b> <br> Today's Paper</p>
    <br>
  </div>
  <div class="logo-image">
      <img src="NYTimeslogo.png" alt="The New York Times" title="Logo">
  </div>
  <hr style="margin: 1% 2% 1% 2%; width: 95%">
</header>

<div class="main-container">
  <div class="left-column">
    {#each articles.slice(0, 2) as article}
      <img src={"https://www.nytimes.com/" + article.multimedia[0]?.url} alt="Article " width="100%"/>
      <h2>{article.headline.main}</h2>
      <p>{article.snippet}</p>
      <hr />
    {/each}
      <!-- <img src="junicat.png" alt="cat laying on window sill">
      <h2> Exceptuer Sint Occaecat Cupidatat Non Proident </h2>
      <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
      <hr>
     
      <h2> Ut Enim Ad Minim Veniam, Quix Nostrud Excercitation Ulllamco Laboris Nisi Ut Aliquip Ex Ea Commodo Consequat </h2>
      <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
      <hr>
      <br> -->
  </div>

  <div class="mid-column"> 
      <h1> Lorem Ipsum Dolor Sit Amet, Consectetur Adipiscing Elit, Sed Do Eiusmod Tempor Incididunt Ut Labore Et Dolore Magna Aliqua </h1>
      <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. </p>
      <p> Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. </p>
      <hr>

      <img src="BrooklynBridge.png" alt="Brooklyn Bridge in between 2 buildings">
      <h3> Lorem ipsum dolor sit amet, consectetur adipiscing elit </h3>
      <p> Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. </p>
      <br>
  </div>

  <div class="right-column"> 
      <img src="mabelcat.png" alt="crying cat on bed">
      <h2> Loren Ipsum Dolor Sit Amet, Consectetur Adipiscing Elit? </h2>
      <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
      <hr>  
     
      <h2> Lorem Ipsum Dolor Sit Amet, Consectetur Adipiscing Elit, Sed Do Eiusmod Tempor Incididunt Ut Labore Et Dolore Magna Aliqua </h2>
      <p> Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. </p>
      <br>
  </div>

  <div class="side-columns">
      <img src="junicat.png" alt="cat laying on window sill">
      <h2> Exceptuer Sint Occaecat Cupidatat Non Proident </h2>
      <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
      <hr>
     
      <h2> Ut Enim Ad Minim Veniam, Quix Nostrud Excercitation Ulllamco Laboris Nisi Ut Aliquip Ex Ea Commodo Consequat </h2>
      <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p>
      <hr> 

      <img src="mabelcat.png" alt="crying cat on bed">
      <h2> Loren Ipsum Dolor Sit Amet, Consectetur Adipiscing Elit? </h2>
      <p> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. </p> 
      <hr>  
     
      <h2> Lorem Ipsum Dolor Sit Amet, Consectetur Adipiscing Elit, Sed Do Eiusmod Tempor Incididunt Ut Labore Et Dolore Magna Aliqua </h2>
      <p> Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. </p>
  </div>
</div>
<hr style="height: 3px; background-color:black; margin: 2% 2% 3% 2%;">

