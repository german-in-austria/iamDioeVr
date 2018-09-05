<template>
	<div class="card">
		<div class="card-header text-white bg-primary text-center">
			<div class="d-flex mb-2">
				<div>Runde {{ rundeNr }}</div>
				<div class="mx-auto">Sprachbeispiel {{ beispielNr }}</div>
				<div class="hidden">Runde {{ rundeNr }}</div>
			</div>
			<button @click="played += 1" type="button" class="btn btn-sm btn-light" :disabled="playing" v-if="played < 2">{{ ((played === 0) ? 'Abspielen' : 'Noch einmal hören?') }}</button>
			<button @click="" type="button" class="btn btn-sm btn-light" disabled v-else>Kann nur zwei mal angehört werden</button>
		</div>
		<div class="card-body" style="background: #eee;">
			<div v-for="aOrt in gData.orte">{{ aOrt.s }} - {{ aOrt.t }}</div>
		</div>
		<div class="card-body">
			<RadioFromTo v-model="sympathie" label="Das Gehörte wirkt auf mich:" from="sympathisch" to="unsympathisch" :disabled="played === 0"/>
		</div>
		<div class="card-footer text-white bg-primary text-right">
			<button @click="" type="button" class="btn btn-sm btn-light" :disabled="played === 0 || sympathie === 0">Weiter</button>
		</div>
	</div>
</template>

<script>
	/* global gData */
	import RadioFromTo from '../formular/RadioFromTo'

	export default {
		name: 'Game',
		data () {
			return {
				beispielNr: 1,
				rundeNr: 1,
				played: 0,
				playing: false,
				sympathie: 0,
				gData: gData,
			}
		},
		components: {
			RadioFromTo,
		},
	}
</script>

<style scoped>
	.hidden {
		visibility: hidden;
	}
</style>
