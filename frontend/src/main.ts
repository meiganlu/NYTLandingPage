import { mount } from 'svelte'
import './app.css'
import App from './App.svelte'

const app = mount(App, {
  target: document.getElementById('app')!,
})

export default app

const currdate = new Date();
const len = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
const format = currdate.toLocaleDateString('en-US', len);
document.getElementById('curr-date').textContent = format;
