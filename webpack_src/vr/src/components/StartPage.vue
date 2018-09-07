<template>
	<div class="text-center">
		<img src="static/vr/pic/i-am-dioe-logo.png" alt="I am DiÖ" title="I am DiÖ" class="dioelogo mx-5">
		<h1>Varietäten raten</h1>
		<br>
		<p>Klingt Deutsch in Österreich überall gleich?</p>
		<p>Absolut nicht, und wir finden das gut so!</p>
		<p>Wie steht es um Ihre Fähigkeit, Deutsch in Österreich in seinen unterschiedlichen<br>
			Ausprägungsarten zu erkennen und gewissen Orten zuzuordnen?</p>
		<p>Wollten Sie immer schon einmal wissen, wie gut Sie darin sind und sich vielleicht sogar mit anderen vergleichen?</p>
		<p>Oder wollen Sie einfach nur mal reinhören, wie vielfältig Deutsch in Österreich sein kann?</p>
		<p>Hier haben Sie nun die Möglichkeit – Wir wünschen viel Vergnügen!</p>
		<br>
		<button @click="$emit('start')" type="button" class="btn btn-primary">Starten ...</button>
	</div>
</template>

<script>
	export default {
		name: 'StartPage',
		data () {
			return {
			}
		},
	}
</script>

<style scoped>
	.dioelogo {
		max-width: 600px;
	}
</style>
