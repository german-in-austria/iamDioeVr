<template>
	<div class="text-center" v-if="site === 0">
		<h1>Vorwort</h1>
		<p>Sie werden gleich verschiedene Wenkersätze hören.</p>
		<p>Diese Sätze wurden von verschiedenen Sprecherinnen und Sprechern aus ganz Österreich eingesprochen.</p>
		<p>Auf der Karte sehen Sie die Orte,<br>
		in denen unsere Sprecherinnen und Sprecher zu Hause sind.</p>
		<p>Karte ...</p>
		<p><b>Ziel des Spiel</b> ist es,<br>
		die Sprecherinnen und Sprecher ihrem Heimatort richtig zuzuordnen.</p>
		<p>Am Ende des Spiels zeigen wir Ihnen,<br>
		wie gut Ihre Einschätzung – im Vergleich mit anderen Spielenden – war.</p>
		<br>
		<button @click="site = 1" type="button" class="btn btn-primary">Weiter zur Anleitung</button>
	</div>
	<div class="text-center" v-else-if="site === 1">
		<h1>Anleitung</h1>
		<p>Und so geht’s:</p>
		<p><b>1)	Gut zuhören!</b><br>
		Hören Sie sich das Sprachbeispiel an.</p>
		<p><b>2)	Richtig zuordnen!</b><br>
		Klicken Sie auf den Ort, von dem Sie glaube, <br>
		dass er der Heimatort des Sprechers/der Sprecherin ist.</p>
		<p><b>3)	Sympathie bewerten!</b><br>
		Beurteilen Sie, wie sympathisch das Sprachbeispiel auf sie wirkt.</p>
		<p>Danach hören Sie auch schon das nächste Sprachbeispiel!</p>
		<p><b>Gut zu wissen:</b><br>
		Eine Runde besteht aus 2 x 6 Sprachbeispielen.<br>
		Sie können sich jedes Sprachbeispiel zweimal anhören.<br>
		Orte können in einer Runde auch mehrmals gewählt werden.</p>
		<br>
		<button @click="site = 2" type="button" class="btn btn-primary">Alles klar!</button>
	</div>
	<Game @getGameData="getGameData" v-else-if="site === 2"/>
</template>

<script>
	import Game from './GamePage/Game'

	export default {
		name: 'GamePage',
		data () {
			return {
				site: 0,
			}
		},
		methods: {
			getGameData (target) {
				this.$emit('getGameData', target)
			},
		},
		components: {
			Game,
		},
	}
</script>

<style scoped>
</style>
