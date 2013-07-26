var Router = Backbone.Router.extend ({
	routes: {
		'': 'portfolio',
		'about': 'about',
		'news': 'news',
		'contact': 'contact',
		'indevelopment': 'indevelopment',

		'subscribe': 'subscribe',
		'login': 'login',

	},
	portfolio: function () {
		$('#backbone-app').html('Portfolio Screen');
	},
	news: function () {
		$('#backbone-app').html('News Screen');
	},
	contact: function () {
		$('#backbone-app').html('Contact Screen');
	},
	about: function () {
		$('#backbone-app').html('About Screen');
	},
	indevelopment: function () {
		$('#backbone-app').html('In Development Screen');
	},

	subscribe: function () {
		$('#backbone-app').html('Subscription Form');
	},
	login: function () {
		$('#backbone-app').html('Login Form');
	}
});

var app = new Router();

$(function() {
	Backbone.history.start();
});
