<template>

	<Info @next="site = 'game'" v-if="site === 'info'"/>

	<Game @getGameData="getGameData" @saveGameRound="saveGameRound" @gameEnd="site = 'gameEnd'" v-else-if="site === 'game'"/>

	<div class="text-center" v-else-if="site === 'gameEnd'">
		<h1>Durchgang beendet</h1>
		<p>...</p>
		<br>
		<button @click="site = 'game'" type="button" class="btn btn-success">Noch einmal spielen</button>
		<button @click="site = 'spracheinstellung'" type="button" class="btn btn-primary">Nicht mehr spielen (Weiter zu den Ergebnissen)</button>
	</div>

	<div class="text-center" v-else-if="site === 'spracheinstellung'">
		<h1>Spracheinstellung</h1>
		<p>...</p>
		<br>
		<button @click="site = 'detailergebnis'" type="button" class="btn btn-primary">Weiter zu den Detailergebnissen</button>
	</div>

	<div class="text-center" v-else-if="site === 'detailergebnis'">
		<h1>Detailergebnis</h1>
		<p>...</p>
		<br>
		<button @click="reload" type="button" class="btn btn-primary">Ende</button>
	</div>

</template>

<script>
	import Info from './GamePage/Info'
	import Game from './GamePage/Game'

	export default {
		name: 'GamePage',
		data () {
			return {
				site: 'info',
				devMode: (process.env.NODE_ENV === 'development'),
			}
		},
		mounted () {
			if (this.devMode) {
				this.site = 'game'
			}
		},
		methods: {
			getGameData (target) {
				this.$emit('getGameData', target)
			},
			saveGameRound (data) {
				this.$emit('saveGameRound', data)
			},
			reload () {
				location.reload()
			}
		},
		components: {
			Info,
			Game,
		},
	}
</script>

<style scoped>
</style>
