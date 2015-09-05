'use strict';

angular.module('myApp.landing', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/landing', {
    templateUrl: 'landing/landing.html',
    controller: 'landingCtrl'
  });
}])

.controller('landingCtrl', [function() {

}]);