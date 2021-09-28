# This file must not be executed. It contains useful commands examples.

# Archive and un-archive notations:
tar -czvf notations.tar.gz notations_*
tar -zxvf notations.tar.gz
# Archive and un-archive input data:
tar -czvf input_data_5e13m-2.tar.gz input_data_5e13m-2
tar -czvf input_data_5e14m-2.tar.gz input_data_5e14m-2
tar -czvf input_data_5e15m-2.tar.gz input_data_5e15m-2
tar -zxvf input_data_5e13m-2.tar.gz
tar -zxvf input_data_5e14m-2.tar.gz
tar -zxvf input_data_5e15m-2.tar.gz
# Archive and un-archive input maps:
tar -czvf input_maps_5e13m-2.tar.gz input_maps_5e13m-2
tar -czvf input_maps_5e14m-2.tar.gz input_maps_5e14m-2
tar -czvf input_maps_5e15m-2.tar.gz input_maps_5e15m-2
tar -zxvf input_maps_5e13m-2.tar.gz
tar -zxvf input_maps_5e14m-2.tar.gz
tar -zxvf input_maps_5e15m-2.tar.gz
# Archive and un-archive input analyses:
tar -czvf input_analyses_5e13m-2.tar.gz input_analyses_5e13m-2
tar -czvf input_analyses_5e14m-2.tar.gz input_analyses_5e14m-2
tar -czvf input_analyses_5e15m-2.tar.gz input_analyses_5e15m-2
tar -zxvf input_analyses_5e13m-2.tar.gz
tar -zxvf input_analyses_5e14m-2.tar.gz
tar -zxvf input_analyses_5e15m-2.tar.gz
# Archive and un-archive output data:
tar -czvf output_data_5e13m-2.tar.gz output_data_5e13m-2
tar -czvf output_data_5e14m-2.tar.gz output_data_5e14m-2
tar -czvf output_data_5e15m-2.tar.gz output_data_5e15m-2
tar -zxvf output_data_5e13m-2.tar.gz
tar -zxvf output_data_5e14m-2.tar.gz
tar -zxvf output_data_5e15m-2.tar.gz
# Archive and un-archive output fits:
tar -czvf output_fits_5e13m-2.tar.gz output_fits_5e13m-2
tar -czvf output_fits_5e14m-2.tar.gz output_fits_5e14m-2
tar -czvf output_fits_5e15m-2.tar.gz output_fits_5e15m-2
tar -zxvf output_fits_5e13m-2.tar.gz
tar -zxvf output_fits_5e14m-2.tar.gz
tar -zxvf output_fits_5e15m-2.tar.gz

# to repatriate files from the root node to the front of the cluster
scp -r /scratch/becht-83073/* becht@centaure:/export/home/becht/transit

# Clear scratch repositories on the cluster:
ssh compute-0-1; cd /scratch/; rm becht* -r;
ssh compute-0-2; cd /scratch/; rm becht* -r;
ssh compute-0-3; cd /scratch/; rm becht* -r;
ssh compute-0-4; cd /scratch/; rm becht* -r;
ssh compute-0-5; cd /scratch/; rm becht* -r;
ssh compute-0-6; cd /scratch/; rm becht* -r;
ssh compute-0-7; cd /scratch/; rm becht* -r;
ssh compute-0-8; cd /scratch/; rm becht* -r;
ssh compute-0-9; cd /scratch/; rm becht* -r;
ssh compute-0-10; cd /scratch/; rm becht* -r;
ssh compute-0-11; cd /scratch/; rm becht* -r;
ssh compute-0-12; cd /scratch/; rm becht* -r;
ssh compute-0-13; cd /scratch/; rm becht* -r;
ssh compute-0-14; cd /scratch/; rm becht* -r;
ssh compute-0-15; cd /scratch/; rm becht* -r;
ssh compute-0-16; cd /scratch/; rm becht* -r;
ssh compute-0-17; cd /scratch/; rm becht* -r;
ssh compute-0-18; cd /scratch/; rm becht* -r;
ssh compute-0-19; cd /scratch/; rm becht* -r;
ssh compute-0-20; cd /scratch/; rm becht* -r;
ssh compute-0-21; cd /scratch/; rm becht* -r;
ssh compute-0-22; cd /scratch/; rm becht* -r;
ssh compute-0-23; cd /scratch/; rm becht* -r;
ssh compute-0-24; cd /scratch/; rm becht* -r;
ssh compute-0-25; cd /scratch/; rm becht* -r;
ssh compute-0-26; cd /scratch/; rm becht* -r;
ssh compute-0-27; cd /scratch/; rm becht* -r;
ssh compute-0-28; cd /scratch/; rm becht* -r;
