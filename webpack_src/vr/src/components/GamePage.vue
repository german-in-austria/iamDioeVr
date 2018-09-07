<template>

	<Info @next="site = 'game'" v-if="site === 'info'"/>

	<Game @getGameData="getGameData" @saveGameRound="saveGameRound" @gameEnd="site = 'gameEnd'" v-else-if="site === 'game'"/>

	<div class="text-center" v-else-if="site === 'gameEnd'">
		<h1>Durchgang beendet</h1>
		<br>
		<br>
		<button @click="site = 'game'" type="button" class="btn btn-success">Noch einmal spielen</button>
		<button @click="site = 'spracheinstellung'" type="button" class="btn btn-primary">Nicht mehr spielen (Weiter zu den Ergebnissen)</button>
	</div>

	<Spracheinstellung @next="site = 'detailergebnis'" @savedataSe="savedataSe" v-else-if="site === 'spracheinstellung'"/>

	<Detailergebnis @getAuswertungsData="getAuswertungsData" @next="reload" v-else-if="site === 'detailergebnis'"/>

</template>

<script>
	import Info from './GamePage/Info'
	import Game from './GamePage/Game'
	import Spracheinstellung from './GamePage/Spracheinstellung'
	import Detailergebnis from './GamePage/Detailergebnis'

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
			getAuswertungsData (target) {
				this.$emit('getAuswertungsData', target)
			},
			saveGameRound (data) {
				this.$emit('saveGameRound', data)
			},
			reload () {
				location.reload()
			},
			savedataSe (data) {
				this.$emit('savedataSe', data)
			}
		},
		components: {
			Info,
			Game,
			Spracheinstellung,
			Detailergebnis,
		},
	}
</script>

<style scoped>
</style>
