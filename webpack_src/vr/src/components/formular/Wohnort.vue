<template>
	<div class="form-group mb-0">
		<label :for="'iWohnort' + _uid">{{ label }}</label>
		<div class="form-row">
			<div class="form-group col-sm-8 col-md-9"><input v-model="value.ort" type="text" class="form-control" :id="'iWohnort' + _uid" placeholder="Wohnort"></div>
			<div class="form-group col-sm-4 col-md-3"><input v-model="value.plz" type="number" min="0" class="form-control" placeholder="Postleitzahl"></div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'Wohnort',
	props: ['label', 'value'],
	data () {
		return {
		}
	},
}
</script>

<style scoped>
</style>
