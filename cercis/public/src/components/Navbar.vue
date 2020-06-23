<template>
    <div id="navbar">
        <b-navbar toggleable="lg" type="dark" variant="primary">
            <b-container fluid>
                <b-navbar-brand href="#">cercis</b-navbar-brand>
                <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
                <b-collapse id="nav-collapse" is-nav>
                    <b-navbar-nav>
                        <b-nav-item :href="config.home()"><i class="fas fa-home"></i> Home</b-nav-item>
                        <b-nav-item :href="config.about()"><i class="fas fa-info"></i> About</b-nav-item>

                        <b-nav-item
                            :href="config.core('poodle', 'detail', 'crystal-creeks-conspiracy-of-kings-bcat-star-cgca')">
                            <i class="fas fa-paw"></i> Basil
                        </b-nav-item>
                        <b-nav-item :href="config.core('poodle', 'detail', 'theory-thick-as-thieves')">
                            <i class="fas fa-paw"></i> Irene
                        </b-nav-item>

                    </b-navbar-nav>
                    <!-- Right aligned nav items -->
                    <b-navbar-nav class="ml-auto">
                        <b-nav-item :href="config.core('poodle', 'all')"><i class="fas fa-paw"></i> Poodles</b-nav-item>
                        <b-nav-item-dropdown right>
                            <!-- Using 'button-content' slot -->
                            <template v-slot:button-content>
                                <em>User</em>
                            </template>
                            <div v-if="request.user.is_authenticated">
                                <b-dropdown-item v-if="user.is_super_user" :href="config.admin()"><i
                                        class="fas fa-cogs"></i> Admin
                                </b-dropdown-item>

                                <b-dropdown-item :href="config.users(request.user.username)">
                                    <i class="fas fa-user"></i>
                                    {% trans "My Profile" %}
                                </b-dropdown-item>
                                <b-dropdown-item :href="config.accounts('logout')">
                                    <i class="fas fa-sign-out-alt"></i>
                                    Logout
                                </b-dropdown-item>
                            </div>
                            <div v-else>
                                <b-dropdown-item :href="config.accounts('login')">
                                    <i class="fas fa-sign-out-alt"></i>
                                    Login
                                </b-dropdown-item>
                                <b-dropdown-item :href="config.account('signup')">
                                    <i class="fas fa-user-plus"></i>
                                    Signup
                                </b-dropdown-item>
                            </div>
                        </b-nav-item-dropdown>
                    </b-navbar-nav>
                </b-collapse>
            </b-container>
        </b-navbar>
    </div>
</template>


<script>
    import configuration from './../configuration.js'
    let config = configuration.endpoints;
    export default {
        props: [

        ],
        components: {

        },
        computed: {

        },
        data: function () {
            return {
                config: config
            }
        }
    }
</script>