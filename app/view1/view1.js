'use strict';

angular.module('myApp.view1', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/view1', {
    templateUrl: 'view1/view1.html',
    controller: 'View1Ctrl'
  });
}])

.controller('View1Ctrl', ['$scope', 'Upload', '$timeout', function ($scope, Upload, $timeout) {
	$scope.lol = function(){
		alert("numb");
	};

    $scope.f;
    $scope.myForm;
    
	$scope.uploadFiles = function(file) {
        $scope.f = file;
        console.log('done');
        console.log(file);
        console.log(file.$error);
        if (file && !file.$error) {
            file.upload = Upload.upload({
                url: 'https://angular-file-upload-cors-srv.appspot.com/upload',
                file: file
            });

            file.upload.then(function (response) {
                $timeout(function () {
                    file.result = response.data;
                });
            }, function (response) {
                if (response.status > 0)
                    $scope.errorMsg = response.status + ': ' + response.data;
            });

            file.upload.progress(function (evt) {
                file.progress = Math.min(100, parseInt(100.0 * 
                                                       evt.loaded / evt.total));
                console.log(file.progress);
            });
        }   
        else{
            console.log('Error');
        }
    };


}]);