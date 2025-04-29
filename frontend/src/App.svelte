<script lang="ts">
  import { onMount } from 'svelte';

  let today = '';

  onMount(() => {
    const now = new Date();
    today = now.toLocaleDateString('en-US', {
      weekday: 'long',
      month: 'long',
      day: 'numeric',
      year: 'numeric',
    });
  });
</script>

<main>
  <header>
    <div class="date">
      <p>
        <b>{today}</b><br />
        Today’s Paper
      </p>
    </div>
    <div class="logo-image">
      <img src="/NYTimeslogo.png" alt="The New York Times logo" />
    </div>
    <hr style="margin: 1% 2% 1% 2%; width: 95%" />
  </header>

  <div class="main-container">
    <!-- left column -->
    <div class="left-column">
      <img src="/junicat.png" alt="cat laying on window sill" />
      <h2>Exceptuer Sint Occaecat Cupidatat Non Proident</h2>
      <p>Lorem ipsum dolor sit amet...</p>
      <hr />
    </div>

    <!-- mid column -->
    <div class="mid-column">
      <h1>Lorem Ipsum Dolor Sit Amet...</h1>
      <p>Lorem ipsum dolor sit amet...</p>
      <hr />
      <img src="/BrooklynBridge.png" alt="Brooklyn Bridge" />
      <h3>Lorem ipsum dolor sit amet...</h3>
      <p>Lorem ipsum dolor sit amet...</p>
    </div>

    <!-- right column -->
    <div class="right-column">
      <img src="/mabelcat.png" alt="crying cat" />
      <h2>Lorem Ipsum...</h2>
      <p>Lorem ipsum dolor sit amet...</p>
      <hr />
    </div>
  </div>

  <hr style="height: 3px; background-color: black; margin: 2% 2% 3% 2%" />
</main>
