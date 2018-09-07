<template>
	<div class="text-center">
		<img src="static/vr/pic/i-am-dioe-logo.png" alt="I am DiÖ" title="I am DiÖ" class="dioelogo mx-5">
		<h1>Varietäten raten</h1>
		<br>
		<p></p>
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
