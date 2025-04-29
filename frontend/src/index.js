const currdate = new Date();
const len = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
const format = currdate.toLocaleDateString('en-US', len);
document.getElementById('curr-date').textContent = format;