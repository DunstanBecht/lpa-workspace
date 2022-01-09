# This file must not be executed. It contains useful commands examples.

# Archive and un-archive notations:
nohup tar -czvf notations.tar.gz notations_* > compress_notations.txt &
nohup tar -zxvf notations.tar.gz > decompress_notations.txt &
# Archive and un-archive input data:
nohup tar -czvf inputs.tar.gz inputs_* > compress_inputs.txt &
nohup tar -zxvf inputs.tar.gz > decompress_inputs.txt &
# Archive and un-archive input maps:
nohup tar -czvf maps.tar.gz maps_* > compress_maps.txt &
nohup tar -zxvf maps.tar.gz > decompress_maps.txt &
# Archive and un-archive input analyses:
nohup tar -czvf stats.tar.gz stats_* > compress_stats.txt &
nohup tar -zxvf stats.tar.gz > decompress_stats.txt &
# Archive and un-archive output data:
nohup tar -czvf outputs.tar.gz outputs_* > compress_outputs.txt &
nohup tar -zxvf outputs.tar.gz > decompress_outputs.txt &
# Archive and un-archive output fits:
nohup tar -czvf fits.tar.gz fits_* > compress_fits.txt &
nohup tar -zxvf fits.tar.gz > decompress_fits.txt &

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
