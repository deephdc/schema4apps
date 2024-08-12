# Changelog

## [2.0.0](https://github.com/ai4os/ai4-metadata/compare/1.0.0...v2.0.0) (2024-08-12)


### ⚠ BREAKING CHANGES

* rename old package to ai4-metadata
* update model metadata schema

### Features

* add base model link ([24763ed](https://github.com/ai4os/ai4-metadata/commit/24763ed031d5c1f84c689e02062d6c09d01d3f83))
* add DOI field ([3e053a3](https://github.com/ai4os/ai4-metadata/commit/3e053a34a1330cfa1d04647716e0a54bf40ff153))
* add ID to schema version ([fe08b68](https://github.com/ai4os/ai4-metadata/commit/fe08b68101a5bf8f8f00aa9ec66a4a6c1cf1d19e))
* add metadata_version to schemata and add CLI option ([5ab9c0e](https://github.com/ai4os/ai4-metadata/commit/5ab9c0e6b0f9cd7710094e4d14850d59c13d8bd5))
* added tools into topics ([a5fbfba](https://github.com/ai4os/ai4-metadata/commit/a5fbfbadffdb31035d839b944c470081794d2d2b))
* additional categories, tasks and data-type ([fb095e1](https://github.com/ai4os/ai4-metadata/commit/fb095e1fa24fa699dced7752dac8f4cbf5033edb))
* description should be a string ([9b3df7c](https://github.com/ai4os/ai4-metadata/commit/9b3df7c5d5d601b2a3323280c8dc45d2d4dea02c))
* do not add a license in the metadata, as repo should have one ([410624b](https://github.com/ai4os/ai4-metadata/commit/410624b5c262c9de6a27c550b7a15de7a8c8da6c))
* docker_image should not be mandatory ([aa36fd5](https://github.com/ai4os/ai4-metadata/commit/aa36fd5e43f9df5ed32859184efe93435896a059))
* fail if keywords still exist ([b422091](https://github.com/ai4os/ai4-metadata/commit/b422091335ef75b28beef1c97bcbab4361b86cca))
* include migration tool ([263f4ef](https://github.com/ai4os/ai4-metadata/commit/263f4ef7577eb81ee20f1ac64d759c5f4a1d8916))
* license should be an enum ([605fa2d](https://github.com/ai4os/ai4-metadata/commit/605fa2d1b0e4577bf11997f195531ec3b5dd2abc))
* print some output for valid instances ([79708e1](https://github.com/ai4os/ai4-metadata/commit/79708e1008e120d7df2349e799bb6c80040d298c))
* rename old package to ai4-metadata ([e7544cf](https://github.com/ai4os/ai4-metadata/commit/e7544cf90590facd819b49bf3ae8dd6bc01d82fe))
* split keywords in three different attributes ([4d9b7ef](https://github.com/ai4os/ai4-metadata/commit/4d9b7ef847813d4178223f500c9eb9223cba3041))
* update model metadata schema ([4e4e7cd](https://github.com/ai4os/ai4-metadata/commit/4e4e7cd050ad23aa2a06cd4c0ddeb99e304c6e96))
* Use an array for dates ([9c4b47b](https://github.com/ai4os/ai4-metadata/commit/9c4b47b1b194e2baab2c0fe554964919b1d9608c))


### Bug Fixes

* add pattern and example to version field ([ec3635d](https://github.com/ai4os/ai4-metadata/commit/ec3635d8102950f6d4b7d9af61d89fe3db18033e))
* add unit testing skeleton ([ef56a6b](https://github.com/ai4os/ai4-metadata/commit/ef56a6bb29882dc9adc44e9b7525c840d0ac88a4))
* add user friendly identifiers ([797c5fa](https://github.com/ai4os/ai4-metadata/commit/797c5fa689b241b3c3ea6d7252e5e055dafcd549))
* change main to master branch ([1f9f2ae](https://github.com/ai4os/ai4-metadata/commit/1f9f2aee7a0276bc8304940d89def538395122cd))
* change release type to python ([b9d6b50](https://github.com/ai4os/ai4-metadata/commit/b9d6b5007989f1680dcdf1ded9c05e9549849717))
* dates should be created not creation ([96b876f](https://github.com/ai4os/ai4-metadata/commit/96b876f2bc2793984268163bb9130eec4d73e78f))
* dates should be updated, not update ([3a9cb53](https://github.com/ai4os/ai4-metadata/commit/3a9cb5391506a364a77d126120171e6c1b7c04e0))
* fix sample for V2 ([71fdd7c](https://github.com/ai4os/ai4-metadata/commit/71fdd7c5db72916b80393e07e4eb1dd5b3996dce))
* fix unit tests style ([6a79785](https://github.com/ai4os/ai4-metadata/commit/6a79785fc06c60f155fc3257c793a08056ba79ce))
* include JSON schemata files in package ([0bd033b](https://github.com/ai4os/ai4-metadata/commit/0bd033bc2522fc74dc0eba4de4ab6856c1dce5e5))
* make black happy ([1f715a5](https://github.com/ai4os/ai4-metadata/commit/1f715a58482b8559114c89869f383be11597e04b))
* merge strings ([e20d8f2](https://github.com/ai4os/ai4-metadata/commit/e20d8f202d719eacd518389118fd00ea9db02e44))
* phrases should end with a period ([4ebfd38](https://github.com/ai4os/ai4-metadata/commit/4ebfd387f4d7a75f1d52688299eca3b556a4efbd))
* remove redundant comments ([22a2181](https://github.com/ai4os/ai4-metadata/commit/22a21816be4a73ac7c7f392ebb53e6625ad2e957))
* restructure code, add unit tests ([8b2cc8c](https://github.com/ai4os/ai4-metadata/commit/8b2cc8ca87abfa36a17f6b2c3ab8297d37f34927))
* use not-required correctly ([d1ec930](https://github.com/ai4os/ai4-metadata/commit/d1ec93001eb410366bb767ebdd47699d051b3f17))
