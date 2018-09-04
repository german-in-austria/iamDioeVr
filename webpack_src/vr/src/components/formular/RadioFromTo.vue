<template>
	<div :class="'form-group' + ((disabled) ? ' disabled' : '')">
		<label>{{ label }}</label>
		<div :class="'form-control ' + (inputClass || '')" style="height:auto; position:relative;">
			<div class="row">
				<div class="col-md-3">{{ from }}</div>
				<div class="col-md-6">
					<div class="d-flex justify-content-center radio-flex">
						<template v-for="i in [1, 2, 3, 4, 5, 6, 7]">
							<div class="flex-fill radio-spacer" v-if="i > 1"></div>
							<input v-model="aValue" class="form-check-input position-static radio" :name="'radioft' + _uid" type="radio" :value="i" :disabled="disabled">
						</template>
					</div>
				</div>
				<div class="col-md-3 text-right">{{ to }}</div>
			</div>
			<div class="invalid-tooltip" style="display: block; top: calc( 100% - 1rem ); left: 5px;" v-if="error && error.error && error.msg && error.changed">{{ error.msg }}</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'RadioFromTo',
	props: ['label', 'from', 'to', 'value', 'inputClass', 'error', 'disabled'],
	data () {
		return {
			aValue: null,
		}
	},
	watch: {
		'aValue' (nVal) {
			this.$emit('input', nVal)
		},
		'value' (nVal) {
			this.aValue = nVal
		},
	},
	mounted () {
		this.aValue = this.value
	},
}
</script>

<style scoped>
	.radio-spacer {
		background: #000;
		height: 2px;
		margin-top: 10px;
		margin-right: 10px;
		margin-left: 10px;
	}
	.radio {
		width: 20px;
		height: 20px;
		margin-top: 1px;
		margin-left: 0px;
	}
	.radio-flex {
		min-height: 20px;
	}
	.disabled {
		opacity: 0.5;
	}
</style>
