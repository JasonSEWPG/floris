# Copyright 2019 NREL

# Licensed under the Apache License, Version 2.0 (the "License"); you may not use
# this file except in compliance with the License. You may obtain a copy of the
# License at http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

# See read the https://floris.readthedocs.io for documentation

import matplotlib.pyplot as plt
import floris.tools as wfct
from floris.utilities import Vec3

# Initialize the FLORIS interface fi
fi = wfct.floris_utilities.FlorisInterface("example_input_curl.json")

# Change the layout
D = fi.floris.farm.flow_field.turbine_map.turbines[0].rotor_diameter
layout_x = [0, 7*D, 14*D]
layout_y = [0, 0, 0]
fi.reinitialize_flow_field(layout_array=(layout_x, layout_y))

# Calculate wake
fi.calculate_wake(yaw_angles=[25,0,0])

# Initialize the horizontal cut
hor_plane = wfct.cut_plane.HorPlane(
    fi.get_flow_data(),
    fi.floris.farm.turbines[0].hub_height
)

# Plot and show
fig, ax = plt.subplots()
wfct.visualization.visualize_cut_plane(hor_plane, ax=ax)


# Get the vertical cut through and visualize
cp = wfct.cut_plane.CrossPlane(fi.get_flow_data(),10*D)
fig, ax = plt.subplots(figsize=(10,10))
wfct.visualization.visualize_cut_plane(cp, ax=ax)
wfct.visualization.visualize_quiver(cp,ax=ax,downSamp=1)
ax.set_ylim([15,300])

# Save the flow data as vtk
fi.get_flow_data().save_as_vtk('for_3d_viz.vtk')

plt.show()
