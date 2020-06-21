const ctn = document.getElementById('btn-4B');
const cd = document.querySelector('.CD');
const br = document.querySelector('.BR');
const back_btn = document.querySelector('#back_a');

ctn.addEventListener('click', () => {
	br.classList.add('animate__animated', 'animate__fadeOut');
	br.style.setProperty('--animate-duration', '0.5s');
	cd.classList.add('animate__animated', 'animate__fadeIn');

	cd.style.setProperty('--animate-duration', '0.5s');
	cd.style.display = 'block';
	back_btn.href = '#';
});

back_btn.addEventListener('click', (e) => {
	if (back_btn.href[back_btn.href.length - 1] == '#') {
		e.preventDefault();
		cd.className = cd.className.replace(
			/\banimate__fadeOut\b/g,
			'animate__fadeIn'
		);
		cd.style.setProperty('--animate-duration', '0.2s');
		br.className = br.className.replace(
			/\banimate__fadeOut\b/g,
			'animate__fadeIn'
		);
		br.style.setProperty('--animate-duration', '0.2s');
		cd.style.display = 'none';
		back_btn.href = './index.html';
	}
});
