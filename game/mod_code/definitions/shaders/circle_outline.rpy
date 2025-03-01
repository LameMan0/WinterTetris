# Unused.
init python:
    renpy.register_shader("wm.circle_outline", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;

        uniform float u_radius;
        uniform float u_segments;
        uniform float u_border;
        uniform vec4 u_color;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        #define PI  3.141592
        #define TAU 6.283185

        float theta(vec2 point) {
            float angle = atan(point.y, point.x);
            angle += TAU * float(angle < 0.0);
            return angle;
        }

        float circle(float radius, float d) {
            return 1.0 - clamp(d - radius, 0.0, 1.0);
        }
    """, fragment_200="""
        vec2 uv = v_tex_coord.xy * res0.xy;
        vec2 from_center = uv - res0.xy / 2.0;

        float d = length(from_center);

        float circle1 = circle(u_radius, d);
        float circle2 = u_border > 0.0 ? circle(u_radius - u_border, d) : 0.0;

        float dash = mod(floor(u_segments * theta(from_center) / PI + 0.5), 2.0);
        float coeff = clamp(circle1 - circle2 - dash, 0.0, 1.0);

        vec4 color = mix(vec4(0.0), u_color, coeff);
        gl_FragColor = vec4(color.rgb * color.a, color.a);
    """)

    renpy.register_shader("wm.circle_outline_normalized", variables="""
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;

        uniform float u_radius;
        uniform float u_segments;
        uniform float u_border;
        uniform vec4 u_color;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_functions="""
        #define PI  3.141592
        #define TAU 6.283185

        float theta(vec2 point) {
            float angle = atan(point.y, point.x);
            angle += TAU * float(angle < 0.0);
            return angle;
        }

        float circle(float radius, float d) {
            return smoothstep(radius * 1.003, radius * 0.997, d);
        }
    """, fragment_200="""
        float aspect = res0.x / res0.y;
        float deno = min(res0.x, res0.y);

        vec2 uv = v_tex_coord.xy;
        uv.x *= aspect;

        vec2 center = vec2(0.5 * aspect, 0.5);
        vec2 from_center = uv - center;

        float d = length(from_center);

        float radius = u_radius / deno;

        float circle1 = circle(radius, d);
        float circle2 = u_border > 0.0 ? circle(radius - (u_border / deno), d) : 0.0;

        float dash = mod(floor(u_segments * theta(from_center) / PI + 0.5), 2.0);
        float coeff = clamp(circle1 - circle2 - dash, 0.0, 1.0);

        vec4 color = mix(vec4(0.0), u_color, coeff);
        gl_FragColor = vec4(color.rgb, color.a) * coeff;
    """)