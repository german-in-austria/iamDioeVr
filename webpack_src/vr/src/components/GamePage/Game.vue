<template>
	<div class="card" v-if="gameData.game && !gameData.game.loading && gameData.game.ready && gameData.game.data">
		<div class="card-header text-white bg-primary text-center">
			<div class="d-flex mb-2">
				<div>Runde {{ rundeNr + 1 }}</div>
				<div class="mx-auto">Sprachbeispiel {{ beispielNr + 1 }}</div>
				<div class="hidden">Runde {{ rundeNr + 1 }}</div>
			</div>
			<button @click="played += 1" type="button" class="btn btn-sm btn-light" :disabled="playing" v-if="played < 2">{{ ((played === 0) ? 'Abspielen' : 'Noch einmal hören?') }}</button>
			<button @click="" type="button" class="btn btn-sm btn-light" disabled v-else>Kann nur zwei mal angehört werden</button>
			{{ gameData.game.data[['S', 'D'][rundeNr]][beispielNr].file }}
		</div>
		<div class="card-body" style="background: #eee;">
			<div class="ort-btn" v-for="aOrt in gData.orte">{{ aOrt.s }} - {{ aOrt.t }}</div>
		</div>
		<div class="card-body">
			<RadioFromTo v-model="sympathie" label="Das Gehörte wirkt auf mich:" from="sympathisch" to="unsympathisch" :disabled="played === 0"/>
		</div>
		<div class="card-footer text-white bg-primary text-right">
			<button @click="" type="button" class="btn btn-sm btn-light" :disabled="played === 0 || sympathie === 0">Weiter</button>
		</div>
	</div>
	<div v-else>
		<br><br><br>
		<h1 class="text-center">Lade ...</h1>
	</div>
</template>

<script>
	/* global gData */
	import RadioFromTo from '../formular/RadioFromTo'

	export default {
		name: 'Game',
		data () {
			return {
				beispielNr: 0,
				rundeNr: 0,
				played: 0,
				playing: false,
				sympathie: 0,
				gData: gData,
				gameData: {},
			}
		},
		mounted () {
			this.$emit('getGameData', this.gameData)
		},
		components: {
			RadioFromTo,
		},
	}
</script>

<style scoped>
	.ort-btn {
		background: #ddd;
		margin: 5px;
		padding: 0px 5px;
		cursor: pointer;
	}
	.ort-btn:hover {
		background: #dde;
	}
	.hidden {
		visibility: hidden;
	}
</style>
