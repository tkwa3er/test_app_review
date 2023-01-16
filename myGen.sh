location="$1"
echo "Give me the name of the module:   "
read folder_name
mkdir "$location/server/src/$folder_name"
cd "$location/server/src/$folder_name"
touch "$folder_name.controller.ts"
touch "$folder_name.module.ts"
touch "$folder_name.resolver.ts"
touch "$folder_name.service.ts"
mkdir base
cd base
touch "$folder_name.ts"
cd ..
code .
