export const Routes = {
  HOME: "/",
  CLIENTS: {
    LIST: "/clients",
    CREATE: "/clients/create",
    EDIT: "/clients/:id",
    EDIT_PARAM: (id?: number) => `/clients/${id}`,
  },
  APPS: {
    LIST: "/apps",
    CREATE: "/apps/create",
    EDIT: "/apps/:id/edit",
    EDIT_PARAM: (id?: number) => `/apps/${id}/edit`,
  },
  CATEGORIAS: {
    LIST: "/categorias",
    CREATE: "/categorias/create",
    EDIT: "/categorias/:id",
    EDIT_PARAM: (id?: number) => `/categorias/${id}`,
  },
  SCREENSHOT: {
    LIST: "/screenshots",
    CREATE: "/screenshots/create",
    EDIT: "/screenshots/:id",
    EDIT_PARAM: (id?: number) => `/screenshots/${id}`,
  },
  CATEGORIA_X_APP: {
    LIST: "/categoriaxapp",
    CREATE: "/categoriaxapp/create",
    EDIT: "/categoriaxapp/:id",
    EDIT_PARAM: (id?: number) => `/categoriaxapp/${id}`,
  },
};
