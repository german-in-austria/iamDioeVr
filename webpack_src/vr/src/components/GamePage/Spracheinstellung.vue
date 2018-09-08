<template>
	<div>
		<h1 class="text-center">3 letzte Fragen</h1>
		<br>
		<div class="alert alert-primary" role="alert">
			Bevor es zu den Ergebnissen geht, haben wir noch 3 letzte Fragen an Sie:
		</div>

		<div class="form-row">
			<div class="form-group col-md-6">
				<label for="inputDialektSympathisch">Diesen Dialekt finde ich besonders sympathisch *</label>
				<input v-model="daten.dialektSympathisch" type="text" :class="'form-control' + ((error.dialektSympathisch.error) ? ' is-invalid' : ' is-valid')" id="inputDialektSympathisch" placeholder="Dialekt">
				<div class="invalid-tooltip" v-if="error.dialektSympathisch.changed">{{ error.dialektSympathisch.msg }}</div>
			</div>
			<div class="form-group col-md-6">
				<label for="inputDialektSympathischWarum">Warum? *</label>
				<input v-model="daten.dialektSympathischWarum" type="text" class="form-control" id="inputDialektSympathischWarum" placeholder="Weil ...">
			</div>
		</div>
		<div class="form-row">
			<div class="form-group col-md-6">
				<label for="inputDialektUnsympathisch">Diesen Dialekt finde ich überhaupt nicht sympathisch *</label>
				<input v-model="daten.dialektUnsympathisch" type="text" :class="'form-control' + ((error.dialektUnsympathisch.error) ? ' is-invalid' : ' is-valid')" id="inputDialektUnsympathisch" placeholder="Dialekt">
				<div class="invalid-tooltip" v-if="error.dialektUnsympathisch.changed">{{ error.dialektUnsympathisch.msg }}</div>
			</div>
			<div class="form-group col-md-6">
				<label for="inputDialektUnsympathischWarum">Warum? *</label>
				<input v-model="daten.dialektUnsympathischWarum" type="text" class="form-control" id="inputDialektUnsympathischWarum" placeholder="Weil ...">
			</div>
		</div>
		<div class="form-group" style="position: relative;">
			<label for="inputGehoerteDialekte">Diese(n) Dialekt(e) habe ich in den Sprachbeispielen gehört *</label>
			<input v-model="daten.gehoerteDialekte" type="text" :class="'form-control' + ((error.gehoerteDialekte.error) ? ' is-invalid' : ' is-valid')" id="inputGehoerteDialekte" placeholder="Gehörte Dialekte">
			<div class="invalid-tooltip" v-if="error.gehoerteDialekte.changed">{{ error.gehoerteDialekte.msg }}</div>
		</div>

		<div class="alert alert-danger mt-3" role="alert" v-if="errors > 0">
			<h5>Formular enthält Fehler:</h5>
			<ul class="mb-0">
				<li v-for="aError in error" v-if="aError.error">{{ aError.msg }}</li>
			</ul>
		</div>

		<button @click="nextStep()" type="button" class="btn btn-primary w-100" :disabled="errors > 0">Weiter zu den Detailergebnissen</button>

	</div>
</template>

<script>
	import _ from 'lodash'

	export default {
		name: 'Spracheinstellung',
		data () {
			return {
				errors: 0,
				daten: {
					dialektSympathisch: '',
					dialektSympathischWarum: '',
					dialektUnsympathisch: '',
					dialektUnsympathischWarum: '',
					gehoerteDialekte: ''
				},
				error: {
					dialektSympathisch: {
						check: function (val) { return val },
						msg: 'Bitte geben Sie an welchen Dialekt Sie besonders sympathisch fanden!'
					},
					// dialektSympathischWarum: {
					// 	check: function (val) { return val },
					// 	msg: 'Bitte geben Sie an warum Sie diesen Dialekt so sympathisch fanden!'
					// },
					dialektUnsympathisch: {
						check: function (val) { return val },
						msg: 'Bitte geben Sie an welchen Dialekt Sie besonders unsympathisch fanden!'
					},
					// dialektUnsympathischWarum: {
					// 	check: function (val) { return val },
					// 	msg: 'Bitte geben Sie an warum Sie diesen Dialekt so unsympathisch fanden!'
					// },
					gehoerteDialekte: {
						check: function (val) { return val },
						msg: 'Bitte geben Sie an welche Dialekte Sie gehört haben!'
					},
				}
			}
		},
		methods: {
			checkErrors () {
				this.errors = 0
				Object.keys(this.daten).forEach(function (aKey) {
					this.checkError(aKey)
					if (this.error[aKey].error) {
						this.errors += 1
					}
				}, this)
			},
			checkError (aKey, uVal = undefined) {
				let cVal = uVal
				if (cVal === undefined) {
					cVal = this.daten[aKey]
				}
				if (!this.error[aKey]) {
					this.error[aKey] = {}
				}
				this.$set(this.error[aKey], 'error', false)
				if (this.error[aKey].check) {
					if (!this.error[aKey].check(cVal, this.weitereAngaben)) {
						this.$set(this.error[aKey], 'error', true)
					}
				}
				this.$set(this.error[aKey], 'empty', true)
				if (cVal) {
					if (typeof cVal === 'object') {
						Object.keys(cVal).some(function (aProp) {
							if (cVal[aProp]) {
								this.$set(this.error[aKey], 'empty', false)
								return true
							}
						}, this)
					} else {
						this.$set(this.error[aKey], 'empty', false)
					}
				}
			},
			debouncedCheckErrors: _.debounce(function () {
				this.checkErrors()
			}, 250),
			initCheckErrors () {
				this.checkErrors()
				Object.keys(this.error).forEach(function (aKey) {
					if (this.daten[aKey] && typeof this.daten[aKey] === 'object') {
						Object.keys(this.daten[aKey]).forEach(function (aProp) {
							if (this.daten[aKey][aProp] || this.daten[aKey][aProp] === 0 || this.daten[aKey][aProp] === '') {
								this.$watch('daten.' + aKey + '.' + aProp, function (nVal) { this.$nextTick(() => { this.$set(this.error[aKey], 'changed', true); this.debouncedCheckErrors() }) })
							}
						}, this)
					} else {
						this.$watch('daten.' + aKey, function (nVal) { this.$nextTick(() => { this.$set(this.error[aKey], 'changed', true); this.debouncedCheckErrors() }) })
					}
				}, this)
			},
			nextStep () {
				if (this.errors === 0) {
					this.$emit('savedataSe', JSON.parse(JSON.stringify(this.daten)))
					this.$nextTick(() => { this.$emit('next') })
				} else {
					alert('Das Formular enthält noch Fehler!')
				}
			},
		},
		mounted () {
			this.initCheckErrors()
		},
	}
</script>

<style scoped>
</style>
