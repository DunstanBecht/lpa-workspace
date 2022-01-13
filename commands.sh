# This file must not be executed. It contains useful commands examples.

# Generate input files:
nohup python3 files.py > nohup_execute_files.txt &
# Archive and un-archive notations:
nohup tar -czvf notations.tar.gz notations_* > nohup_compress_notations.txt &
nohup tar -zxvf notations.tar.gz > nohup_decompress_notations.txt &
# Archive and un-archive input data:
nohup tar -czvf inputs.tar.gz inputs_* > nohup_compress_inputs.txt &
nohup tar -zxvf inputs.tar.gz > nohup_decompress_inputs.txt &

# Generate maps:
nohup python3 maps.py <cycle-identifier> > nohup_execute_maps.txt &
# Archive and un-archive input maps:
nohup tar -czvf maps.tar.gz maps_* > nohup_compress_maps.txt &
nohup tar -zxvf maps.tar.gz > nohup_decompress_maps.txt &

# Run input analysis:
mpirun -n 10 python3 stats.py
# Archive and un-archive input analyses:
nohup tar -czvf stats.tar.gz stats_* > nohup_compress_stats.txt &
nohup tar -zxvf stats.tar.gz > nohup_decompress_stats.txt &

# Run simulations:
nohup python3 fits.py <cycle-identifier> > nohup_execute_fits.txt &
# Archive and un-archive output data:
nohup tar -czvf outputs.tar.gz outputs_* > nohup_compress_outputs.txt &
nohup tar -zxvf outputs.tar.gz > nohup_decompress_outputs.txt &

# Average output files:
nohup python3 average.py <cycle-identifier> > nohup_execute_average.txt &
# Archive and un-archive output data:
nohup tar -czvf average.tar.gz average_* > nohup_compress_average.txt &
nohup tar -zxvf average.tar.gz > nohup_decompress_average.txt &

# Run fits:
nohup python3 fits.py <cycle-identifier> > nohup_execute_fits.txt &
# Archive and un-archive output fits:
nohup tar -czvf fits.tar.gz fits_* > nohup_compress_fits.txt &
nohup tar -zxvf fits.tar.gz > nohup_decompress_fits.txt &

# to repatriate files from the root node to the front of the cluster
scp -r /scratch/becht-83073/* becht@centaure:/export/home/becht/transit
