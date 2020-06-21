const ctn = document.getElementById('btn-4E');
const ed = document.querySelector('.ED');
const er = document.querySelector('.ER');
const back_btn = document.querySelector('#back_a');

ctn.addEventListener('click', () => {
	er.classList.add('animate__animated', 'animate__fadeOut');
	er.style.setProperty('--animate-duration', '0.5s');
	ed.classList.add('animate__animated', 'animate__fadeIn');

	ed.style.setProperty('--animate-duration', '0.5s');
	ed.style.display = 'block';
	back_btn.href = '#';
});

back_btn.addEventListener('click', (e) => {
	if (back_btn.href[back_btn.href.length - 1] == '#') {
		e.preventDefault();
		ed.className = ed.className.replace(
			/\banimate__fadeOut\b/g,
			'animate__fadeIn'
		);
		ed.style.setProperty('--animate-duration', '0.2s');
		er.className = er.className.replace(
			/\banimate__fadeOut\b/g,
			'animate__fadeIn'
		);
		er.style.setProperty('--animate-duration', '0.2s');
		ed.style.display = 'none';
		back_btn.href = './index.html';
	}
});
