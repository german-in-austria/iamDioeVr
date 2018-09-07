<template>
	<div class="form-group mb-0">
		<label :for="'iWohnort' + _uid">{{ label }}</label>
		<div class="form-row">
			<div class="form-group col-sm-8 col-md-8"><input v-model="value.ort" type="text" :class="'form-control ' + (inputClass || '')" :id="'iWohnort' + _uid" placeholder="Wohnort"></div>
			<div class="form-group col-sm-4 col-md-4"><input v-model="value.plz" type="number" min="0" :class="'form-control ' + inputClass" placeholder="Postleitzahl"></div>
			<div class="invalid-tooltip" style="display: block; top: calc( 100% - 1rem ); left: 5px;" v-if="error && error.error && error.msg && error.changed">{{ error.msg }}</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'Wohnort',
	props: ['label', 'value', 'inputClass', 'error'],
	data () {
		return {
		}
	},
}
</script>

<style scoped>
</style>
